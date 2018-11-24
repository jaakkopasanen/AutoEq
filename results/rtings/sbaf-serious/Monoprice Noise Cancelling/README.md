# Monoprice Noise Cancelling

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 21 0.0; 23 0.8; 25 0.3; 28 -0.4; 31 -1.0; 34 -1.5; 37 -1.9; 41 -2.3; 45 -2.7; 49 -3.0; 54 -3.3; 60 -3.6; 66 -3.8; 72 -4.0; 79 -4.2; 87 -4.5; 96 -4.9; 106 -5.4; 116 -5.7; 128 -6.0; 141 -6.1; 155 -6.1; 170 -6.1; 187 -6.0; 206 -5.8; 227 -5.5; 249 -5.2; 274 -5.0; 302 -4.9; 332 -4.7; 365 -4.6; 402 -4.5; 442 -4.7; 486 -5.0; 535 -4.6; 588 -4.0; 647 -3.9; 712 -4.1; 783 -4.0; 861 -2.6; 947 -0.8; 1042 0.5; 1146 -0.0; 1261 -0.7; 1387 -0.1; 1526 -0.3; 1678 -1.3; 1846 -0.8; 2031 0.6; 2234 1.2; 2457 2.1; 2703 3.3; 2973 3.4; 3270 3.3; 3597 4.6; 3957 5.2; 4353 3.6; 4788 4.7; 5267 4.5; 5793 2.9; 6373 5.1; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monoprice Noise Cancelling GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-59**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monoprice Noise Cancelling ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 114 Hz  | 0.47 | -3.5 dB |
| Peaking | 206 Hz  | 0.52 | -2.9 dB |
| Peaking | 585 Hz  | 1.26 | -3.0 dB |
| Peaking | 3906 Hz | 1.31 | 5.0 dB  |
| Peaking | 6414 Hz | 6.64 | 3.6 dB  |
| Peaking | 19 Hz   | 2.39 | 1.9 dB  |
| Peaking | 819 Hz  | 4.2  | -2.7 dB |
| Peaking | 946 Hz  | 2.22 | 2.2 dB  |
| Peaking | 1721 Hz | 5.91 | -1.9 dB |
| Peaking | 8400 Hz | 3.65 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Monoprice%20Noise%20Cancelling/Monoprice%20Noise%20Cancelling.png)