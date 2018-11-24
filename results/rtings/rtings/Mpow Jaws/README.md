# Mpow Jaws

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -2.8; 23 -2.9; 25 -2.9; 28 -3.0; 31 -3.0; 34 -3.0; 37 -3.1; 41 -3.2; 45 -3.2; 49 -3.3; 54 -3.5; 60 -4.0; 66 -4.4; 72 -4.8; 79 -5.3; 87 -5.8; 96 -6.4; 106 -7.0; 116 -7.5; 128 -8.1; 141 -8.5; 155 -8.8; 170 -8.8; 187 -8.8; 206 -8.7; 227 -8.5; 249 -8.3; 274 -7.7; 302 -6.7; 332 -5.5; 365 -4.9; 402 -4.7; 442 -4.5; 486 -4.0; 535 -3.2; 588 -2.3; 647 -1.4; 712 -0.5; 783 0.3; 861 0.3; 947 0.1; 1042 0.2; 1146 -0.2; 1261 -0.2; 1387 0.2; 1526 0.8; 1678 1.3; 1846 1.8; 2031 2.6; 2234 4.0; 2457 5.7; 2703 6.0; 2973 6.0; 3270 6.0; 3597 5.5; 3957 4.7; 4353 3.7; 4788 4.2; 5267 6.0; 5793 5.2; 6373 3.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 -0.4; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Mpow Jaws GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Mpow Jaws ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.14 | -2.5 dB |
| Peaking | 131 Hz  | 0.9  | -3.8 dB |
| Peaking | 242 Hz  | 0.76 | -6.1 dB |
| Peaking | 2943 Hz | 1.39 | 6.4 dB  |
| Peaking | 5500 Hz | 3.32 | 4.8 dB  |
| Peaking | 344 Hz  | 4.37 | 0.9 dB  |
| Peaking | 482 Hz  | 2.11 | -1.2 dB |
| Peaking | 788 Hz  | 2.46 | 1.5 dB  |
| Peaking | 1288 Hz | 3.6  | -0.7 dB |
| Peaking | 9448 Hz | 2.83 | -0.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Mpow%20Jaws/Mpow%20Jaws.png)