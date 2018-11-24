# Jaybird X2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.9dB
GraphicEQ: 21 0.0; 23 2.1; 25 2.1; 28 1.9; 31 1.8; 34 1.7; 37 1.6; 41 1.5; 45 1.4; 49 1.3; 54 1.1; 60 0.7; 66 0.4; 72 0.3; 79 0.0; 87 -0.3; 96 -0.6; 106 -1.2; 116 -1.7; 128 -2.1; 141 -2.5; 155 -2.7; 170 -3.0; 187 -3.1; 206 -3.1; 227 -3.0; 249 -2.7; 274 -2.3; 302 -1.7; 332 -1.1; 365 -0.5; 402 -0.1; 442 0.5; 486 1.1; 535 1.7; 588 2.2; 647 2.7; 712 2.8; 783 2.4; 861 1.5; 947 0.5; 1042 -0.3; 1146 -0.7; 1261 -1.0; 1387 -1.4; 1526 -1.9; 1678 -1.9; 1846 -1.5; 2031 -0.9; 2234 -0.4; 2457 0.1; 2703 0.4; 2973 1.0; 3270 2.1; 3597 2.8; 3957 2.1; 4353 1.0; 4788 2.1; 5267 4.0; 5793 5.7; 6373 5.1; 7010 2.5; 7711 -0.4; 8482 -4.2; 9330 -5.5; 10263 -5.3; 11289 -4.3; 12418 -1.5; 13660 0.0; 15026 0.0; 16529 -0.2; 18182 -3.3; 20000 -3.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jaybird X2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-58**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jaybird X2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 197 Hz   | 1.18 | -3.5 dB |
| Peaking | 650 Hz   | 2.48 | 3.4 dB  |
| Peaking | 6142 Hz  | 1.91 | 7.3 dB  |
| Peaking | 9352 Hz  | 1.88 | -7.5 dB |
| Peaking | 19064 Hz | 2.44 | -4.2 dB |
| Peaking | 23 Hz    | 1.12 | 2.2 dB  |
| Peaking | 48 Hz    | 1.9  | 1.0 dB  |
| Peaking | 1607 Hz  | 2.17 | -2.3 dB |
| Peaking | 3475 Hz  | 5.52 | 2.3 dB  |
| Peaking | 24000 Hz | 1.62 | -0.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Jaybird%20X2/Jaybird%20X2.png)