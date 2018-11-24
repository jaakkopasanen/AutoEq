# Jaybird Tarah

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.6dB
GraphicEQ: 21 0.0; 23 0.7; 25 0.6; 28 0.4; 31 0.3; 34 0.3; 37 0.2; 41 0.1; 45 -0.0; 49 -0.1; 54 -0.2; 60 -0.5; 66 -0.7; 72 -0.9; 79 -1.0; 87 -1.1; 96 -1.4; 106 -2.0; 116 -2.7; 128 -3.6; 141 -4.1; 155 -4.4; 170 -4.4; 187 -4.4; 206 -4.3; 227 -4.1; 249 -3.6; 274 -3.0; 302 -2.3; 332 -1.7; 365 -1.2; 402 -0.6; 442 -0.0; 486 0.6; 535 1.2; 588 1.7; 647 2.1; 712 2.5; 783 2.4; 861 2.0; 947 0.9; 1042 -0.6; 1146 -1.6; 1261 -2.0; 1387 -2.7; 1526 -3.5; 1678 -3.8; 1846 -3.8; 2031 -4.2; 2234 -4.6; 2457 -5.0; 2703 -4.5; 2973 -2.4; 3270 0.3; 3597 1.9; 3957 1.6; 4353 0.2; 4788 0.4; 5267 0.2; 5793 -1.5; 6373 -7.8; 7010 -5.2; 7711 -0.2; 8482 -0.1; 9330 -4.7; 10263 -6.0; 11289 -0.2; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jaybird Tarah GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-26**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jaybird Tarah ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 183 Hz   | 0.96 | -4.8 dB |
| Peaking | 700 Hz   | 1.75 | 3.5 dB  |
| Peaking | 1947 Hz  | 1.46 | -5.0 dB |
| Peaking | 6576 Hz  | 8.42 | -9.1 dB |
| Peaking | 9848 Hz  | 6.84 | -7.2 dB |
| Peaking | 17 Hz    | 0.65 | 0.8 dB  |
| Peaking | 2022 Hz  | 3.06 | 3.3 dB  |
| Peaking | 2640 Hz  | 1.32 | -4.8 dB |
| Peaking | 3527 Hz  | 2.12 | 5.5 dB  |
| Peaking | 12129 Hz | 4.15 | 0.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Jaybird%20Tarah/Jaybird%20Tarah.png)