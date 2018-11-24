# Nuforce NE 600X

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.5dB
GraphicEQ: 21 -13.2; 23 -13.1; 25 -13.0; 28 -12.8; 31 -12.6; 34 -12.3; 37 -12.1; 41 -11.9; 45 -11.7; 49 -11.5; 54 -11.2; 60 -11.0; 66 -10.9; 72 -10.7; 79 -10.5; 87 -10.3; 96 -10.2; 106 -9.9; 116 -9.5; 128 -9.2; 141 -8.8; 155 -8.4; 170 -8.0; 187 -7.4; 206 -6.9; 227 -6.2; 249 -5.7; 274 -5.1; 302 -4.4; 332 -3.8; 365 -3.2; 402 -2.6; 442 -1.9; 486 -1.5; 535 -1.0; 588 -0.2; 647 0.0; 712 0.3; 783 0.7; 861 0.5; 947 0.2; 1042 -0.1; 1146 -0.5; 1261 -0.9; 1387 -1.6; 1526 -2.4; 1678 -3.1; 1846 -3.5; 2031 -3.9; 2234 -4.5; 2457 -4.9; 2703 -5.2; 2973 -4.5; 3270 -3.0; 3597 -1.4; 3957 -2.6; 4353 -6.0; 4788 -6.2; 5267 -3.0; 5793 1.5; 6373 4.1; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -0.6; 10263 -2.0; 11289 -0.0; 12418 0.0; 13660 -0.0; 15026 -1.4; 16529 -0.9; 18182 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Nuforce NE 600X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-44**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Nuforce NE 600X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 21 Hz    | 0.19 | -12.8 dB |
| Peaking | 160 Hz   | 0.73 | -4.1 dB  |
| Peaking | 2417 Hz  | 1.64 | -5.1 dB  |
| Peaking | 4692 Hz  | 4.36 | -6.8 dB  |
| Peaking | 6390 Hz  | 4.8  | 5.7 dB   |
| Peaking | 788 Hz   | 1.94 | 1.7 dB   |
| Peaking | 1617 Hz  | 4.52 | -1.2 dB  |
| Peaking | 9994 Hz  | 6.04 | -2.6 dB  |
| Peaking | 12781 Hz | 1.02 | 0.8 dB   |
| Peaking | 15567 Hz | 2.32 | -2.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Nuforce%20NE%20600X/Nuforce%20NE%20600X.png)