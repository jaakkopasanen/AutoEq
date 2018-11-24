# Jaybird X2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.4dB
GraphicEQ: 21 0.0; 23 1.8; 25 1.8; 28 1.8; 31 1.8; 34 1.8; 37 1.7; 41 1.7; 45 1.7; 49 1.6; 54 1.4; 60 1.0; 66 0.6; 72 0.3; 79 -0.1; 87 -0.6; 96 -1.1; 106 -1.7; 116 -2.2; 128 -2.7; 141 -3.0; 155 -3.3; 170 -3.6; 187 -3.7; 206 -3.6; 227 -3.5; 249 -3.3; 274 -3.0; 302 -2.5; 332 -2.0; 365 -1.6; 402 -1.1; 442 -0.6; 486 -0.1; 535 0.5; 588 1.1; 647 1.7; 712 2.0; 783 1.9; 861 1.3; 947 0.5; 1042 -0.3; 1146 -0.9; 1261 -1.3; 1387 -1.4; 1526 -1.5; 1678 -1.6; 1846 -1.6; 2031 -1.4; 2234 -0.9; 2457 -0.4; 2703 -0.2; 2973 -0.1; 3270 0.3; 3597 0.7; 3957 0.9; 4353 1.0; 4788 2.3; 5267 3.6; 5793 4.3; 6373 2.6; 7010 1.5; 7711 -1.3; 8482 -4.6; 9330 -7.0; 10263 -8.7; 11289 -8.8; 12418 -5.9; 13660 -1.7; 15026 -0.2; 16529 -3.1; 18182 -6.5; 20000 -5.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jaybird X2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-43**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jaybird X2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 201 Hz   | 0.99 | -4.0 dB |
| Peaking | 694 Hz   | 3.08 | 2.7 dB  |
| Peaking | 5840 Hz  | 2.4  | 5.6 dB  |
| Peaking | 10430 Hz | 1.94 | -9.8 dB |
| Peaking | 18838 Hz | 1.95 | -7.3 dB |
| Peaking | 34 Hz    | 0.32 | 2.0 dB  |
| Peaking | 111 Hz   | 1.33 | -1.5 dB |
| Peaking | 854 Hz   | 5.2  | 1.1 dB  |
| Peaking | 1578 Hz  | 1.51 | -1.8 dB |
| Peaking | 24000 Hz | 1.76 | 0.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Jaybird%20X2/Jaybird%20X2.png)