# Shure SE535
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.0; 25 3.9; 28 3.7; 31 3.6; 34 3.5; 37 3.4; 41 3.2; 45 3.0; 49 2.9; 54 2.6; 60 2.3; 66 1.9; 72 1.6; 79 1.2; 87 0.7; 96 0.2; 106 -0.2; 116 -0.6; 128 -1.1; 141 -1.4; 155 -1.7; 170 -1.9; 187 -2.1; 206 -2.2; 227 -2.4; 249 -2.4; 274 -2.5; 302 -2.4; 332 -2.2; 365 -2.1; 402 -2.0; 442 -1.9; 486 -1.7; 535 -1.4; 588 -1.2; 647 -0.9; 712 -0.5; 783 -0.2; 861 0.0; 947 0.1; 1042 -0.0; 1146 -0.1; 1261 0.1; 1387 0.6; 1526 1.3; 1678 2.0; 1846 2.6; 2031 3.3; 2234 4.6; 2457 5.9; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -0.4; 15026 -1.8; 16529 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE535 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE535 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 0.44 | 4.2 dB  |
| Peaking | 67 Hz    | 0.82 | 2.3 dB  |
| Peaking | 188 Hz   | 0.24 | -2.8 dB |
| Peaking | 4706 Hz  | 0.53 | 8.4 dB  |
| Peaking | 8898 Hz  | 0.82 | -4.8 dB |
| Peaking | 1361 Hz  | 2.84 | -1.0 dB |
| Peaking | 2548 Hz  | 3.42 | 1.6 dB  |
| Peaking | 4759 Hz  | 1.16 | -1.1 dB |
| Peaking | 5912 Hz  | 3.87 | 1.9 dB  |
| Peaking | 14408 Hz | 4.26 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Shure%20SE535/Shure%20SE535.png)