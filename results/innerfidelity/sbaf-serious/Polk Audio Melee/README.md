# Polk Audio Melee
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.2; 23 -1.6; 25 -1.9; 28 -2.2; 31 -2.4; 34 -2.6; 37 -2.7; 41 -2.8; 45 -2.9; 49 -3.0; 54 -3.1; 60 -3.2; 66 -3.1; 72 -3.0; 79 -3.0; 87 -3.8; 96 -4.6; 106 -4.1; 116 -3.9; 128 -4.6; 141 -5.6; 155 -5.3; 170 -4.6; 187 -5.5; 206 -5.3; 227 -4.9; 249 -4.5; 274 -3.8; 302 -3.2; 332 -3.2; 365 -3.0; 402 -2.4; 442 -1.9; 486 -1.7; 535 -1.4; 588 -0.8; 647 -0.6; 712 -0.6; 783 -0.4; 861 -0.3; 947 -0.1; 1042 0.1; 1146 0.5; 1261 0.9; 1387 1.0; 1526 1.4; 1678 2.3; 1846 3.8; 2031 5.3; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 5.1; 3957 3.5; 4353 3.5; 4788 3.9; 5267 5.8; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio Melee GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio Melee ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 37 Hz   | 0.81 | -1.3 dB |
| Peaking | 127 Hz  | 0.25 | -1.8 dB |
| Peaking | 178 Hz  | 0.75 | -3.5 dB |
| Peaking | 2644 Hz | 1.22 | 6.6 dB  |
| Peaking | 5754 Hz | 3.26 | 5.5 dB  |
| Peaking | 1603 Hz | 1.95 | -1.7 dB |
| Peaking | 2241 Hz | 1.29 | 2.5 dB  |
| Peaking | 2580 Hz | 3.38 | -2.6 dB |
| Peaking | 6606 Hz | 7.17 | 2.4 dB  |
| Peaking | 7494 Hz | 1.72 | -1.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Polk%20Audio%20Melee/Polk%20Audio%20Melee.png)