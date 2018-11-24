# Grado SR60

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 5.8; 31 4.9; 34 4.0; 37 3.2; 41 2.4; 45 1.6; 49 1.0; 54 0.5; 60 -0.2; 66 -0.4; 72 -0.5; 79 -1.0; 87 -1.4; 96 -1.5; 106 -1.5; 116 -1.5; 128 -1.4; 141 -1.1; 155 -1.0; 170 -1.1; 187 -0.9; 206 -0.5; 227 -0.6; 249 -1.4; 274 -1.3; 302 -1.0; 332 -0.6; 365 -0.4; 402 -0.1; 442 0.0; 486 0.1; 535 0.3; 588 0.3; 647 0.5; 712 0.5; 783 0.4; 861 0.3; 947 0.1; 1042 -0.2; 1146 -0.4; 1261 -0.9; 1387 -1.8; 1526 -2.8; 1678 -3.9; 1846 -4.7; 2031 -5.4; 2234 -5.7; 2457 -5.6; 2703 -4.6; 2973 -2.1; 3270 0.1; 3597 1.4; 3957 -0.1; 4353 -3.4; 4788 -7.7; 5267 -4.2; 5793 -2.6; 6373 -0.6; 7010 -3.3; 7711 -5.7; 8482 -8.1; 9330 -6.8; 10263 -0.4; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -1.6; 16529 -1.2; 18182 -0.4; 20000 -2.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR60 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR60 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 0.89 | 6.7 dB  |
| Peaking | 91 Hz    | 0.6  | -2.0 dB |
| Peaking | 2162 Hz  | 1.85 | -6.1 dB |
| Peaking | 8432 Hz  | 2.88 | -8.2 dB |
| Peaking | 21085 Hz | 2.07 | -6.0 dB |
| Peaking | 749 Hz   | 1.97 | 1.0 dB  |
| Peaking | 3692 Hz  | 4.24 | 4.3 dB  |
| Peaking | 4735 Hz  | 4.34 | -7.2 dB |
| Peaking | 6354 Hz  | 8.16 | 2.2 dB  |
| Peaking | 10762 Hz | 5.81 | 2.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20SR60/Grado%20SR60.png)