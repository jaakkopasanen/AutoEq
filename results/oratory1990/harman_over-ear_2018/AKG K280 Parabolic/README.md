# AKG K280 Parabolic

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 5.1; 106 4.2; 116 3.3; 128 2.5; 141 1.7; 155 1.1; 170 0.5; 187 0.0; 206 -0.4; 227 -0.6; 249 -0.7; 274 -0.7; 302 -0.6; 332 -0.8; 365 -0.7; 402 -0.7; 442 -0.8; 486 -0.8; 535 -0.8; 588 -0.8; 647 -0.9; 712 -0.9; 783 -0.9; 861 -0.8; 947 -0.5; 1042 0.6; 1146 2.3; 1261 3.3; 1387 3.5; 1526 2.9; 1678 1.8; 1846 0.7; 2031 0.8; 2234 2.3; 2457 3.5; 2703 3.8; 2973 3.6; 3270 2.8; 3597 2.3; 3957 3.9; 4353 3.7; 4788 2.3; 5267 -1.7; 5793 2.1; 6373 5.0; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K280 Parabolic GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K280 Parabolic ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 43 Hz    |  0.54 | 7.0 dB  |
| Peaking | 1348 Hz  |  4.55 | 3.6 dB  |
| Peaking | 3101 Hz  |  1.45 | 3.7 dB  |
| Peaking | 6426 Hz  |  7.16 | 4.9 dB  |
| Peaking | 24000 Hz |  2.25 | 2.0 dB  |
| Peaking | 19 Hz    |  1.59 | 3.7 dB  |
| Peaking | 74 Hz    |  0.12 | -2.0 dB |
| Peaking | 90 Hz    |  1.35 | 3.5 dB  |
| Peaking | 4352 Hz  |  5.94 | 2.2 dB  |
| Peaking | 5369 Hz  | 12.28 | -4.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/AKG%20K280%20Parabolic/AKG%20K280%20Parabolic.png)