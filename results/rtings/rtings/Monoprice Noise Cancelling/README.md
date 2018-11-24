# Monoprice Noise Cancelling

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.9dB
GraphicEQ: 21 0.0; 23 0.5; 25 0.1; 28 -0.5; 31 -1.0; 34 -1.4; 37 -1.7; 41 -2.1; 45 -2.4; 49 -2.7; 54 -2.9; 60 -3.3; 66 -3.7; 72 -4.0; 79 -4.4; 87 -4.9; 96 -5.4; 106 -5.9; 116 -6.2; 128 -6.5; 141 -6.7; 155 -6.7; 170 -6.7; 187 -6.6; 206 -6.3; 227 -6.0; 249 -5.8; 274 -5.7; 302 -5.7; 332 -5.6; 365 -5.6; 402 -5.5; 442 -5.8; 486 -6.2; 535 -5.8; 588 -5.0; 647 -4.9; 712 -4.9; 783 -4.5; 861 -2.8; 947 -0.8; 1042 0.4; 1146 -0.2; 1261 -1.0; 1387 -0.0; 1526 0.0; 1678 -0.9; 1846 -0.9; 2031 0.2; 2234 0.7; 2457 1.7; 2703 2.7; 2973 2.3; 3270 1.4; 3597 2.4; 3957 4.0; 4353 3.5; 4788 4.8; 5267 4.0; 5793 1.5; 6373 2.8; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -1.1; 16529 -1.6; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monoprice Noise Cancelling GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-59**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monoprice Noise Cancelling ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 51 Hz    | 1.46 | -0.6 dB |
| Peaking | 146 Hz   | 0.56 | -6.2 dB |
| Peaking | 575 Hz   | 0.8  | -4.7 dB |
| Peaking | 1044 Hz  | 3.89 | 3.1 dB  |
| Peaking | 4398 Hz  | 1.21 | 4.3 dB  |
| Peaking | 19 Hz    | 2.26 | 1.3 dB  |
| Peaking | 2733 Hz  | 5.23 | 1.8 dB  |
| Peaking | 3305 Hz  | 6.25 | -1.5 dB |
| Peaking | 8661 Hz  | 4.54 | -0.9 dB |
| Peaking | 15974 Hz | 4    | -2.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Monoprice%20Noise%20Cancelling/Monoprice%20Noise%20Cancelling.png)