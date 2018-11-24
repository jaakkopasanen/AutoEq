# Denon AH-D2000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.5dB
GraphicEQ: 21 0.0; 23 3.3; 25 2.6; 28 1.9; 31 1.5; 34 1.4; 37 1.5; 41 1.8; 45 1.7; 49 1.5; 54 1.4; 60 1.8; 66 1.9; 72 1.6; 79 1.4; 87 1.1; 96 0.9; 106 0.7; 116 0.5; 128 0.5; 141 0.3; 155 0.2; 170 0.4; 187 0.2; 206 0.4; 227 0.4; 249 0.4; 274 0.6; 302 0.8; 332 0.8; 365 0.9; 402 1.0; 442 0.9; 486 0.9; 535 0.3; 588 -0.2; 647 -0.4; 712 -0.5; 783 0.9; 861 0.4; 947 -0.1; 1042 -0.0; 1146 0.5; 1261 1.2; 1387 1.8; 1526 1.9; 1678 1.7; 1846 1.5; 2031 2.2; 2234 4.2; 2457 5.3; 2703 5.1; 2973 4.0; 3270 2.6; 3597 1.5; 3957 1.1; 4353 2.0; 4788 1.6; 5267 2.5; 5793 1.5; 6373 -0.4; 7010 0.9; 7711 0.3; 8482 0.0; 9330 -2.5; 10263 -4.7; 11289 -0.7; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.3; 18182 -4.8; 20000 -2.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D2000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-55**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D2000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 2556 Hz  | 1.9  | 5.3 dB  |
| Peaking | 5348 Hz  | 5.38 | 2.2 dB  |
| Peaking | 10130 Hz | 6.5  | -5.5 dB |
| Peaking | 18673 Hz | 2.57 | -5.7 dB |
| Peaking | 17 Hz    | 1.31 | 5.2 dB  |
| Peaking | 62 Hz    | 1.12 | 1.5 dB  |
| Peaking | 370 Hz   | 2.18 | 1.0 dB  |
| Peaking | 1407 Hz  | 6.06 | 1.2 dB  |
| Peaking | 15070 Hz | 1.92 | 0.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-D2000/Denon%20AH-D2000.png)