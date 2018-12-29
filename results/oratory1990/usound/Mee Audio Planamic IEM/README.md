# Mee Audio Planamic IEM
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -5.0; 23 -5.2; 25 -5.3; 28 -5.5; 31 -5.6; 34 -5.7; 37 -5.8; 41 -5.9; 45 -6.0; 49 -6.2; 54 -6.3; 60 -6.5; 66 -6.7; 72 -6.9; 79 -7.1; 87 -7.3; 96 -7.4; 106 -7.5; 116 -7.5; 128 -7.5; 141 -7.5; 155 -7.5; 170 -7.3; 187 -6.9; 206 -6.7; 227 -6.8; 249 -6.5; 274 -6.0; 302 -5.4; 332 -4.8; 365 -4.0; 402 -3.3; 442 -3.0; 486 -2.5; 535 -2.0; 588 -1.5; 647 -1.0; 712 -0.5; 783 -0.0; 861 0.2; 947 0.2; 1042 -0.2; 1146 -0.6; 1261 -1.2; 1387 -1.8; 1526 -2.2; 1678 -2.7; 1846 -2.9; 2031 -3.2; 2234 -4.0; 2457 -5.5; 2703 -6.0; 2973 -6.3; 3270 -6.6; 3597 -7.4; 3957 -8.4; 4353 -5.3; 4788 0.1; 5267 4.5; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Mee Audio Planamic IEM GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Mee Audio Planamic IEM ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 37 Hz   | 0.3  | -5.3 dB  |
| Peaking | 133 Hz  | 0.76 | -4.3 dB  |
| Peaking | 271 Hz  | 1.3  | -3.4 dB  |
| Peaking | 3970 Hz | 1.06 | -12.4 dB |
| Peaking | 5552 Hz | 1.97 | 14.0 dB  |
| Peaking | 922 Hz  | 1.39 | 2.9 dB   |
| Peaking | 1013 Hz | 0.6  | -1.6 dB  |
| Peaking | 6516 Hz | 0.59 | 0.8 dB   |
| Peaking | 6518 Hz | 6.52 | 2.9 dB   |
| Peaking | 7056 Hz | 1.74 | -2.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Mee%20Audio%20Planamic%20IEM/Mee%20Audio%20Planamic%20IEM.png)