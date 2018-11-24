# Koss KSC75

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 5.7; 54 4.7; 60 3.4; 66 2.2; 72 1.1; 79 0.2; 87 -0.8; 96 -1.6; 106 -2.2; 116 -2.7; 128 -3.1; 141 -3.3; 155 -3.3; 170 -2.9; 187 -2.7; 206 -2.6; 227 -2.4; 249 -2.2; 274 -2.1; 302 -2.0; 332 -1.9; 365 -1.7; 402 -1.6; 442 -1.5; 486 -1.4; 535 -1.2; 588 -1.0; 647 -0.7; 712 -0.4; 783 -0.2; 861 -0.1; 947 -0.0; 1042 0.0; 1146 -0.0; 1261 -0.3; 1387 -0.9; 1526 -1.7; 1678 -2.5; 1846 -3.8; 2031 -5.1; 2234 -5.4; 2457 -4.9; 2703 -3.8; 2973 -3.2; 3270 -1.9; 3597 3.5; 3957 3.8; 4353 -0.9; 4788 -6.1; 5267 -1.2; 5793 2.6; 6373 1.7; 7010 0.1; 7711 -0.6; 8482 -3.4; 9330 -6.0; 10263 -4.2; 11289 -0.1; 12418 0.0; 13660 -0.3; 15026 -0.1; 16529 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss KSC75 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss KSC75 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 46 Hz    | 0.42 | 10.6 dB |
| Peaking | 101 Hz   | 0.49 | -8.7 dB |
| Peaking | 2216 Hz  | 2.51 | -6.0 dB |
| Peaking | 9443 Hz  | 5.01 | -6.8 dB |
| Peaking | 24000 Hz | 2.26 | -3.2 dB |
| Peaking | 1047 Hz  | 3.72 | 0.7 dB  |
| Peaking | 3116 Hz  | 4.95 | -4.6 dB |
| Peaking | 3775 Hz  | 3.16 | 7.2 dB  |
| Peaking | 4807 Hz  | 5.01 | -8.8 dB |
| Peaking | 5821 Hz  | 4.59 | 4.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Koss%20KSC75/Koss%20KSC75.png)