# Polk Audio Buckle

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -6.8; 23 -6.9; 25 -7.0; 28 -7.0; 31 -7.0; 34 -6.8; 37 -6.7; 41 -6.6; 45 -6.4; 49 -6.1; 54 -5.9; 60 -5.5; 66 -5.2; 72 -4.6; 79 -4.1; 87 -4.2; 96 -4.8; 106 -5.2; 116 -5.0; 128 -4.9; 141 -4.8; 155 -4.6; 170 -3.8; 187 -4.2; 206 -4.2; 227 -4.0; 249 -3.8; 274 -3.0; 302 -1.3; 332 -1.0; 365 -0.3; 402 -0.0; 442 0.3; 486 0.6; 535 0.9; 588 1.3; 647 1.7; 712 1.4; 783 0.7; 861 -0.1; 947 -0.0; 1042 0.1; 1146 0.5; 1261 1.1; 1387 1.5; 1526 1.9; 1678 2.4; 1846 3.2; 2031 3.9; 2234 4.4; 2457 4.9; 2703 5.5; 2973 4.8; 3270 4.5; 3597 5.5; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
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
| Peaking | 21 Hz   | 0.5  | -5.1 dB |
| Peaking | 50 Hz   | 0.47 | -3.2 dB |
| Peaking | 167 Hz  | 1.07 | -3.5 dB |
| Peaking | 2791 Hz | 0.92 | 4.8 dB  |
| Peaking | 5293 Hz | 2.09 | 4.9 dB  |
| Peaking | 248 Hz  | 6.42 | -1.5 dB |
| Peaking | 566 Hz  | 2.21 | 1.6 dB  |
| Peaking | 4087 Hz | 4.61 | 1.7 dB  |
| Peaking | 6391 Hz | 4.04 | 4.5 dB  |
| Peaking | 6704 Hz | 1.3  | -2.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Polk%20Audio%20Buckle/Polk%20Audio%20Buckle.png)