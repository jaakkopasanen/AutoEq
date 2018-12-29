# AKG K280 Parabolic
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 5.9; 49 5.4; 54 4.8; 60 4.1; 66 3.5; 72 3.3; 79 2.9; 87 2.3; 96 1.8; 106 1.3; 116 0.9; 128 0.6; 141 0.3; 155 0.1; 170 -0.1; 187 -0.3; 206 -0.5; 227 -0.6; 249 -0.7; 274 -0.7; 302 -0.6; 332 -0.8; 365 -0.7; 402 -0.7; 442 -0.8; 486 -0.8; 535 -0.8; 588 -0.8; 647 -0.9; 712 -0.9; 783 -0.9; 861 -0.8; 947 -0.5; 1042 0.6; 1146 2.3; 1261 3.3; 1387 3.5; 1526 2.9; 1678 1.8; 1846 0.7; 2031 0.8; 2234 2.3; 2457 3.5; 2703 3.8; 2973 3.6; 3270 2.8; 3597 2.3; 3957 3.9; 4353 3.7; 4788 2.3; 5267 -1.7; 5793 2.1; 6373 5.0; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K280 Parabolic GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K280 Parabolic ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 0.69 | 6.7 dB  |
| Peaking | 1347 Hz  | 4.48 | 3.6 dB  |
| Peaking | 3100 Hz  | 1.44 | 3.7 dB  |
| Peaking | 6411 Hz  | 7.1  | 4.8 dB  |
| Peaking | 24000 Hz | 2.25 | 2.0 dB  |
| Peaking | 563 Hz   | 0.4  | -1.2 dB |
| Peaking | 1171 Hz  | 6.01 | 1.6 dB  |
| Peaking | 3447 Hz  | 4.2  | -4.3 dB |
| Peaking | 3815 Hz  | 1.73 | 3.6 dB  |
| Peaking | 5350 Hz  | 9.49 | -4.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/AKG%20K280%20Parabolic/AKG%20K280%20Parabolic.png)