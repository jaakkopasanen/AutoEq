# Polk Audio Hinge
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.2dB
GraphicEQ: 21 -12.1; 23 -12.3; 25 -12.5; 28 -12.7; 31 -12.8; 34 -12.9; 37 -12.9; 41 -12.9; 45 -13.0; 49 -13.0; 54 -13.1; 60 -13.3; 66 -13.3; 72 -13.3; 79 -13.4; 87 -13.5; 96 -14.0; 106 -14.3; 116 -14.8; 128 -15.1; 141 -15.4; 155 -15.0; 170 -14.4; 187 -14.1; 206 -12.9; 227 -11.4; 249 -10.0; 274 -8.4; 302 -8.3; 332 -8.3; 365 -8.0; 402 -8.2; 442 -8.5; 486 -8.5; 535 -8.1; 588 -7.1; 647 -6.2; 712 -5.4; 783 -3.8; 861 -2.3; 947 -0.7; 1042 0.1; 1146 -1.7; 1261 -4.4; 1387 -6.1; 1526 -7.8; 1678 -7.4; 1846 -6.7; 2031 -8.3; 2234 -7.3; 2457 -5.5; 2703 -4.2; 2973 -3.4; 3270 -3.6; 3597 -2.0; 3957 -1.0; 4353 -3.9; 4788 -5.2; 5267 -2.1; 5793 -0.2; 6373 -1.4; 7010 -4.5; 7711 -3.7; 8482 -0.3; 9330 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio Hinge GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-1**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio Hinge ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.6dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 38 Hz    | 0.28 | -11.4 dB |
| Peaking | 161 Hz   | 0.78 | -9.7 dB  |
| Peaking | 499 Hz   | 1.91 | -5.6 dB  |
| Peaking | 2007 Hz  | 1.15 | -7.5 dB  |
| Peaking | 17 Hz    | 1.07 | -2.0 dB  |
| Peaking | 1031 Hz  | 5.1  | 4.0 dB   |
| Peaking | 1473 Hz  | 5.48 | -2.4 dB  |
| Peaking | 7231 Hz  | 5.66 | -4.6 dB  |
| Peaking | 24000 Hz | 2.42 | -0.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Polk%20Audio%20Hinge/Polk%20Audio%20Hinge.png)