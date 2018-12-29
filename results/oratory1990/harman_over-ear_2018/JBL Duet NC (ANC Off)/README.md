# JBL Duet NC (ANC Off)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.0; 23 -1.6; 25 -1.9; 28 -2.2; 31 -2.3; 34 -2.5; 37 -2.7; 41 -2.8; 45 -2.6; 49 -2.2; 54 -1.6; 60 -0.8; 66 -0.2; 72 0.9; 79 2.3; 87 2.3; 96 1.6; 106 1.3; 116 1.6; 128 1.3; 141 0.4; 155 -0.2; 170 0.4; 187 1.7; 206 3.3; 227 5.5; 249 6.0; 274 6.0; 302 6.0; 332 6.0; 365 6.0; 402 6.0; 442 6.0; 486 5.4; 535 3.7; 588 3.0; 647 2.4; 712 1.5; 783 0.8; 861 0.3; 947 0.0; 1042 0.1; 1146 0.5; 1261 1.3; 1387 1.2; 1526 1.4; 1678 2.7; 1846 3.8; 2031 4.8; 2234 5.6; 2457 5.5; 2703 5.0; 2973 6.0; 3270 5.9; 3597 1.3; 3957 0.6; 4353 1.7; 4788 2.9; 5267 6.0; 5793 2.0; 6373 4.4; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL Duet NC (ANC Off) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL Duet NC (ANC Off) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 81 Hz   |  0.4  | -6.1 dB |
| Peaking | 85 Hz   |  1.19 | 7.5 dB  |
| Peaking | 306 Hz  |  0.92 | 8.4 dB  |
| Peaking | 2537 Hz |  1.68 | 6.0 dB  |
| Peaking | 5345 Hz |  4.37 | 4.8 dB  |
| Peaking | 468 Hz  |  6.43 | 1.8 dB  |
| Peaking | 931 Hz  |  2.77 | -1.5 dB |
| Peaking | 3272 Hz |  6.6  | 4.2 dB  |
| Peaking | 3654 Hz |  3.87 | -3.2 dB |
| Peaking | 6560 Hz | 12.03 | 3.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/JBL%20Duet%20NC%20(ANC%20Off)/JBL%20Duet%20NC%20(ANC%20Off).png)