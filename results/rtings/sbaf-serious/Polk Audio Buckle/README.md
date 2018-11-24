# Polk Audio Buckle

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.3; 23 -1.6; 25 -1.9; 28 -2.2; 31 -2.4; 34 -2.5; 37 -2.5; 41 -2.3; 45 -2.1; 49 -1.9; 54 -1.6; 60 -1.3; 66 -1.0; 72 -0.5; 79 -0.2; 87 0.0; 96 0.1; 106 0.2; 116 0.3; 128 0.4; 141 0.6; 155 0.8; 170 0.8; 187 0.8; 206 0.8; 227 1.0; 249 1.3; 274 1.1; 302 0.4; 332 0.5; 365 1.1; 402 2.2; 442 2.7; 486 2.2; 535 1.7; 588 1.7; 647 1.8; 712 0.6; 783 -0.7; 861 -0.8; 947 -0.4; 1042 0.4; 1146 1.2; 1261 2.0; 1387 2.4; 1526 2.8; 1678 3.4; 1846 4.2; 2031 4.9; 2234 5.9; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio Buckle GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio Buckle ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.91 | -2.6 dB |
| Peaking | 162 Hz  | 0.83 | 0.8 dB  |
| Peaking | 489 Hz  | 1.69 | 2.1 dB  |
| Peaking | 870 Hz  | 2.95 | -2.6 dB |
| Peaking | 3309 Hz | 0.66 | 6.8 dB  |
| Peaking | 326 Hz  | 7.92 | -0.8 dB |
| Peaking | 2241 Hz | 3.99 | 0.9 dB  |
| Peaking | 3290 Hz | 2.47 | -0.9 dB |
| Peaking | 6226 Hz | 2.13 | 5.5 dB  |
| Peaking | 7454 Hz | 1.44 | -4.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Polk%20Audio%20Buckle/Polk%20Audio%20Buckle.png)