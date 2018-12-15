# Mpow Jaws

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -2.8; 23 -2.9; 25 -2.9; 28 -3.0; 31 -3.0; 34 -3.0; 37 -3.1; 41 -3.2; 45 -3.2; 49 -3.3; 54 -3.5; 60 -4.0; 66 -4.4; 72 -4.8; 79 -5.3; 87 -5.8; 96 -6.4; 106 -7.0; 116 -7.5; 128 -8.1; 141 -8.5; 155 -8.8; 170 -8.8; 187 -8.8; 206 -8.7; 227 -8.5; 249 -8.3; 274 -7.7; 302 -6.7; 332 -5.5; 365 -4.9; 402 -4.7; 442 -4.5; 486 -4.0; 535 -3.2; 588 -2.3; 647 -1.4; 712 -0.5; 783 0.3; 861 0.3; 947 0.1; 1042 0.2; 1146 -0.2; 1261 -0.2; 1387 0.2; 1526 0.8; 1678 1.3; 1846 1.8; 2031 2.6; 2234 4.0; 2457 5.6; 2703 6.0; 2973 6.0; 3270 5.6; 3597 4.5; 3957 3.5; 4353 2.4; 4788 2.4; 5267 5.7; 5793 3.1; 6373 2.3; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Mpow Jaws GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Mpow Jaws ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.14 | -2.5 dB |
| Peaking | 137 Hz  | 0.83 | -4.6 dB |
| Peaking | 253 Hz  | 0.8  | -5.4 dB |
| Peaking | 2848 Hz | 1.51 | 6.4 dB  |
| Peaking | 5420 Hz | 5.53 | 4.5 dB  |
| Peaking | 496 Hz  | 3.86 | -1.1 dB |
| Peaking | 800 Hz  | 2.89 | 1.4 dB  |
| Peaking | 1280 Hz | 4.29 | -0.7 dB |
| Peaking | 6809 Hz | 7.55 | 3.4 dB  |
| Peaking | 7007 Hz | 1.88 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Mpow%20Jaws/Mpow%20Jaws.png)