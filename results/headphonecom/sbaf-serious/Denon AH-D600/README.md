# Denon AH-D600

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -0.6; 23 -0.9; 25 -1.2; 28 -1.6; 31 -1.9; 34 -2.1; 37 -2.2; 41 -2.3; 45 -2.3; 49 -2.1; 54 -1.7; 60 -1.7; 66 -2.2; 72 -3.1; 79 -3.5; 87 -3.6; 96 -3.9; 106 -4.1; 116 -4.2; 128 -4.4; 141 -4.5; 155 -4.6; 170 -3.7; 187 -3.9; 206 -3.3; 227 -1.9; 249 -0.4; 274 0.4; 302 0.1; 332 -0.3; 365 -0.0; 402 -0.1; 442 0.5; 486 1.2; 535 0.6; 588 0.6; 647 0.4; 712 0.0; 783 -0.0; 861 0.1; 947 0.0; 1042 -0.0; 1146 -0.1; 1261 -0.5; 1387 -1.2; 1526 -2.0; 1678 -2.5; 1846 -3.0; 2031 -2.7; 2234 -1.1; 2457 -0.8; 2703 -1.1; 2973 -0.5; 3270 0.7; 3597 2.8; 3957 4.2; 4353 5.3; 4788 6.0; 5267 4.6; 5793 2.2; 6373 0.0; 7010 1.9; 7711 0.3; 8482 0.0; 9330 -0.5; 10263 -0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.0; 20000 -0.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D600 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 61 Hz   | 0.31 | -1.6 dB |
| Peaking | 163 Hz  | 0.79 | -6.0 dB |
| Peaking | 249 Hz  | 0.64 | 3.7 dB  |
| Peaking | 1865 Hz | 1.92 | -3.2 dB |
| Peaking | 4590 Hz | 2.62 | 6.6 dB  |
| Peaking | 207 Hz  | 3.81 | -1.4 dB |
| Peaking | 279 Hz  | 1.61 | 1.8 dB  |
| Peaking | 339 Hz  | 2.94 | -1.9 dB |
| Peaking | 2915 Hz | 6.31 | -1.1 dB |
| Peaking | 3694 Hz | 8.59 | 1.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-D600/Denon%20AH-D600.png)