# Panasonic RP-HJE120

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.2dB
GraphicEQ: 21 -1.8; 23 -2.1; 25 -2.4; 28 -2.8; 31 -3.1; 34 -3.3; 37 -3.5; 41 -3.7; 45 -3.9; 49 -4.1; 54 -4.4; 60 -4.9; 66 -5.4; 72 -5.8; 79 -6.3; 87 -6.8; 96 -7.4; 106 -7.9; 116 -8.4; 128 -8.9; 141 -9.2; 155 -9.5; 170 -9.5; 187 -9.4; 206 -9.3; 227 -8.9; 249 -8.4; 274 -7.8; 302 -7.3; 332 -6.9; 365 -6.3; 402 -5.6; 442 -4.8; 486 -3.9; 535 -2.9; 588 -1.9; 647 -0.7; 712 0.3; 783 0.7; 861 0.6; 947 0.1; 1042 -0.1; 1146 -0.4; 1261 -0.6; 1387 -0.7; 1526 -0.9; 1678 -1.2; 1846 -1.6; 2031 -2.0; 2234 -1.8; 2457 -1.4; 2703 -1.3; 2973 -1.2; 3270 -1.0; 3597 -0.8; 3957 -1.1; 4353 -2.2; 4788 -2.9; 5267 -3.6; 5793 -2.3; 6373 -0.4; 7010 2.0; 7711 0.3; 8482 0.0; 9330 -3.4; 10263 -2.5; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -0.1; 16529 -0.8; 18182 0.0; 20000 -1.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Panasonic RP-HJE120 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-21**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Panasonic RP-HJE120 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 100 Hz   | 0.43 | -5.6 dB |
| Peaking | 224 Hz   | 0.79 | -5.9 dB |
| Peaking | 2161 Hz  | 2.53 | -1.8 dB |
| Peaking | 5057 Hz  | 3.47 | -3.6 dB |
| Peaking | 21299 Hz | 1.34 | -1.5 dB |
| Peaking | 25 Hz    | 2    | -0.9 dB |
| Peaking | 423 Hz   | 2.65 | -1.3 dB |
| Peaking | 768 Hz   | 2.63 | 2.4 dB  |
| Peaking | 6996 Hz  | 7.26 | 2.6 dB  |
| Peaking | 9674 Hz  | 7.81 | -4.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Panasonic%20RP-HJE120/Panasonic%20RP-HJE120.png)