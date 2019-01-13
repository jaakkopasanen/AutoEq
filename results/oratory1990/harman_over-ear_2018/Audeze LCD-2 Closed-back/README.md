# Audeze LCD-2 Closed-back
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.1; 25 1.9; 28 1.8; 31 1.6; 34 1.5; 37 1.3; 41 1.1; 45 0.9; 49 0.6; 54 0.5; 60 0.2; 66 -0.0; 72 -0.2; 79 -0.4; 87 -0.6; 96 -1.0; 106 -1.3; 116 -1.6; 128 -1.8; 141 -2.0; 155 -2.0; 170 -2.2; 187 -2.1; 206 -2.0; 227 -1.8; 249 -1.4; 274 -0.9; 302 -0.0; 332 0.8; 365 1.5; 402 1.5; 442 1.2; 486 0.9; 535 0.7; 588 0.6; 647 0.7; 712 0.8; 783 1.0; 861 0.6; 947 0.3; 1042 -0.3; 1146 -0.6; 1261 -0.5; 1387 -1.4; 1526 -2.4; 1678 -2.3; 1846 -2.6; 2031 -2.9; 2234 -1.8; 2457 -1.4; 2703 0.5; 2973 2.7; 3270 5.6; 3597 6.0; 3957 6.0; 4353 5.8; 4788 2.6; 5267 0.8; 5793 -3.2; 6373 -4.1; 7010 -4.7; 7711 -3.7; 8482 0.0; 9330 0.0; 10263 -0.4; 11289 -6.6; 12418 -6.4; 13660 -3.6; 15026 -2.6; 16529 -4.3; 18182 -10.4; 20000 -21.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-2 Closed-back GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-2 Closed-back ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 25 Hz    | 1.67 | 2.4 dB   |
| Peaking | 2103 Hz  | 1.55 | -4.9 dB  |
| Peaking | 3829 Hz  | 1.37 | 8.6 dB   |
| Peaking | 6374 Hz  | 2.23 | -6.6 dB  |
| Peaking | 20044 Hz | 1.18 | -21.4 dB |
| Peaking | 211 Hz   | 0.79 | -3.5 dB  |
| Peaking | 364 Hz   | 0.95 | 3.1 dB   |
| Peaking | 9907 Hz  | 3.02 | 4.6 dB   |
| Peaking | 11609 Hz | 2.76 | -7.4 dB  |
| Peaking | 15594 Hz | 1.99 | 3.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Audeze%20LCD-2%20Closed-back/Audeze%20LCD-2%20Closed-back.png)