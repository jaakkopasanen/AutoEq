# Jaybird X3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.6dB
GraphicEQ: 21 -1.1; 23 -1.1; 25 -1.1; 28 -1.1; 31 -1.1; 34 -1.0; 37 -1.0; 41 -1.0; 45 -1.0; 49 -1.0; 54 -1.1; 60 -1.4; 66 -1.7; 72 -1.9; 79 -2.2; 87 -2.6; 96 -3.0; 106 -3.4; 116 -3.9; 128 -4.2; 141 -4.5; 155 -4.6; 170 -4.5; 187 -4.7; 206 -4.9; 227 -4.8; 249 -4.3; 274 -3.7; 302 -3.2; 332 -2.7; 365 -2.1; 402 -1.6; 442 -0.9; 486 -0.2; 535 0.4; 588 1.0; 647 1.6; 712 1.8; 783 1.7; 861 1.3; 947 0.5; 1042 -0.4; 1146 -0.9; 1261 -1.3; 1387 -1.5; 1526 -1.6; 1678 -2.0; 1846 -2.5; 2031 -3.1; 2234 -3.2; 2457 -3.1; 2703 -2.9; 2973 -1.8; 3270 -0.3; 3597 0.8; 3957 1.4; 4353 1.6; 4788 2.2; 5267 2.4; 5793 1.5; 6373 -2.0; 7010 -6.7; 7711 -5.5; 8482 -0.6; 9330 -0.4; 10263 -4.7; 11289 -4.6; 12418 -0.1; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -1.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jaybird X3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-25**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jaybird X3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 227 Hz   | 0.49 | -7.2 dB  |
| Peaking | 1803 Hz  | 0.17 | 8.0 dB   |
| Peaking | 2036 Hz  | 0.64 | -10.9 dB |
| Peaking | 7219 Hz  | 4.41 | -10.8 dB |
| Peaking | 10835 Hz | 3.76 | -8.0 dB  |
| Peaking | 21 Hz    | 1.58 | -0.9 dB  |
| Peaking | 1163 Hz  | 2.65 | -2.0 dB  |
| Peaking | 2008 Hz  | 0.57 | 1.4 dB   |
| Peaking | 2679 Hz  | 2.5  | -2.2 dB  |
| Peaking | 16076 Hz | 1.47 | -0.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Jaybird%20X3/Jaybird%20X3.png)