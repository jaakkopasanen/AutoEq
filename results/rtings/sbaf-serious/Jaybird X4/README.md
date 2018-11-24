# Jaybird X4

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.7dB
GraphicEQ: 21 -1.0; 23 -1.0; 25 -1.0; 28 -1.0; 31 -1.0; 34 -1.1; 37 -1.1; 41 -1.2; 45 -1.2; 49 -1.2; 54 -1.2; 60 -1.4; 66 -1.5; 72 -1.4; 79 -1.4; 87 -1.4; 96 -1.5; 106 -1.7; 116 -2.5; 128 -3.6; 141 -4.4; 155 -4.6; 170 -4.4; 187 -4.3; 206 -4.2; 227 -3.9; 249 -3.4; 274 -2.7; 302 -2.0; 332 -1.4; 365 -0.9; 402 -0.4; 442 0.2; 486 0.8; 535 1.3; 588 1.8; 647 2.1; 712 2.4; 783 2.2; 861 1.7; 947 0.7; 1042 -0.6; 1146 -1.5; 1261 -2.0; 1387 -2.6; 1526 -3.3; 1678 -3.6; 1846 -3.5; 2031 -3.9; 2234 -4.2; 2457 -4.6; 2703 -4.2; 2973 -2.2; 3270 0.5; 3597 2.3; 3957 2.2; 4353 1.1; 4788 1.6; 5267 2.3; 5793 0.7; 6373 -5.8; 7010 -5.0; 7711 0.0; 8482 0.0; 9330 0.0; 10263 -0.6; 11289 -1.7; 12418 -0.4; 13660 -0.3; 15026 -2.0; 16529 -0.2; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jaybird X4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-26**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jaybird X4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 178 Hz   | 0.88 | -4.7 dB  |
| Peaking | 710 Hz   | 1.23 | 4.1 dB   |
| Peaking | 2790 Hz  | 0.71 | -11.9 dB |
| Peaking | 3656 Hz  | 0.97 | 11.9 dB  |
| Peaking | 6636 Hz  | 7.77 | -8.7 dB  |
| Peaking | 28 Hz    | 0.35 | -0.9 dB  |
| Peaking | 100 Hz   | 3.34 | 1.1 dB   |
| Peaking | 4412 Hz  | 8.96 | -1.5 dB  |
| Peaking | 5395 Hz  | 7.19 | 1.8 dB   |
| Peaking | 15148 Hz | 4.05 | -2.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Jaybird%20X4/Jaybird%20X4.png)