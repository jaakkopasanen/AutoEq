# Beyerdynamic DT 1770 (Leatherette Earpads)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -3.8; 23 -4.0; 25 -4.1; 28 -4.1; 31 -3.9; 34 -3.6; 37 -3.3; 41 -3.1; 45 -2.8; 49 -2.5; 54 -2.7; 60 -3.5; 66 -4.5; 72 -5.6; 79 -6.3; 87 -6.7; 96 -7.4; 106 -7.9; 116 -8.4; 128 -8.6; 141 -7.9; 155 -7.6; 170 -6.8; 187 -4.8; 206 -2.3; 227 -0.3; 249 0.8; 274 0.8; 302 0.2; 332 -0.3; 365 -0.5; 402 -0.6; 442 -0.7; 486 -0.7; 535 -0.5; 588 -0.3; 647 0.2; 712 0.3; 783 0.2; 861 0.0; 947 -0.0; 1042 0.1; 1146 0.3; 1261 0.7; 1387 1.2; 1526 2.0; 1678 3.4; 1846 4.8; 2031 5.3; 2234 5.9; 2457 5.5; 2703 5.4; 2973 6.0; 3270 5.7; 3597 5.6; 3957 6.0; 4353 6.0; 4788 6.0; 5267 3.3; 5793 0.2; 6373 -0.6; 7010 1.9; 7711 -1.7; 8482 -3.1; 9330 -1.2; 10263 -1.2; 11289 -2.2; 12418 -1.2; 13660 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 1770 (Leatherette Earpads) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 1770 (Leatherette Earpads) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 12 Hz    | 0.17 | -3.7 dB |
| Peaking | 121 Hz   | 1.35 | -8.3 dB |
| Peaking | 3157 Hz  | 0.82 | 6.6 dB  |
| Peaking | 8287 Hz  | 3.28 | -4.1 dB |
| Peaking | 11416 Hz | 4.14 | -2.5 dB |
| Peaking | 170 Hz   | 5.25 | -2.4 dB |
| Peaking | 250 Hz   | 3.45 | 3.1 dB  |
| Peaking | 4821 Hz  | 5.67 | 2.6 dB  |
| Peaking | 6169 Hz  | 4.33 | -4.1 dB |
| Peaking | 6760 Hz  | 6.71 | 3.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Beyerdynamic%20DT%201770%20(Leatherette%20Earpads)/Beyerdynamic%20DT%201770%20(Leatherette%20Earpads).png)