# JBL Duet NC (ANC On)

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -7.4; 23 -6.9; 25 -6.4; 28 -5.7; 31 -5.1; 34 -4.5; 37 -4.1; 41 -3.6; 45 -3.2; 49 -3.0; 54 -2.8; 60 -2.7; 66 -2.4; 72 -2.3; 79 -2.1; 87 -1.8; 96 -2.2; 106 -2.4; 116 -2.4; 128 -2.3; 141 -1.8; 155 -1.1; 170 -0.3; 187 0.4; 206 1.1; 227 1.8; 249 2.6; 274 3.5; 302 4.4; 332 4.9; 365 5.1; 402 5.2; 442 5.4; 486 6.0; 535 5.6; 588 5.4; 647 5.2; 712 4.4; 783 3.5; 861 2.3; 947 0.8; 1042 -0.6; 1146 -1.6; 1261 -1.5; 1387 -1.7; 1526 -2.3; 1678 -0.6; 1846 1.0; 2031 2.2; 2234 3.2; 2457 3.0; 2703 2.1; 2973 2.9; 3270 5.8; 3597 4.8; 3957 -0.1; 4353 -0.2; 4788 0.9; 5267 5.8; 5793 -0.3; 6373 3.1; 7010 1.6; 7711 -1.9; 8482 -1.9; 9330 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL Duet NC (ANC On) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL Duet NC (ANC On) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 438 Hz   | 1.06 | 6.5 dB  |
| Peaking | 2306 Hz  | 5.54 | 3.1 dB  |
| Peaking | 3344 Hz  | 5.32 | 6.1 dB  |
| Peaking | 23996 Hz | 2.27 | 1.1 dB  |
| Peaking | 13 Hz    | 0.39 | -8.4 dB |
| Peaking | 120 Hz   | 1.84 | -2.4 dB |
| Peaking | 1334 Hz  | 2.79 | -3.2 dB |
| Peaking | 6917 Hz  | 2.18 | 4.6 dB  |
| Peaking | 7859 Hz  | 3.99 | -5.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/JBL%20Duet%20NC%20(ANC%20On)/JBL%20Duet%20NC%20(ANC%20On).png)