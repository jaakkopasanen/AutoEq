# AKG K601 (Dekoni Sheepskin Earpads)

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.9; 25 4.4; 28 3.7; 31 3.1; 34 2.6; 37 2.1; 41 1.6; 45 1.2; 49 0.8; 54 0.4; 60 -0.1; 66 -0.5; 72 -0.9; 79 -1.3; 87 -1.7; 96 -2.1; 106 -2.5; 116 -2.8; 128 -3.2; 141 -3.6; 155 -3.8; 170 -4.0; 187 -4.2; 206 -4.3; 227 -4.3; 249 -4.2; 274 -3.9; 302 -3.5; 332 -2.9; 365 -2.3; 402 -1.9; 442 -1.2; 486 -0.5; 535 0.1; 588 0.8; 647 1.7; 712 2.2; 783 2.4; 861 1.6; 947 0.4; 1042 -0.1; 1146 -0.4; 1261 -0.7; 1387 -0.6; 1526 -0.7; 1678 -1.1; 1846 -1.7; 2031 -2.7; 2234 -3.7; 2457 -3.8; 2703 -2.4; 2973 1.2; 3270 6.0; 3597 6.0; 3957 5.3; 4353 4.3; 4788 0.6; 5267 -0.9; 5793 -2.0; 6373 -0.3; 7010 0.6; 7711 -1.5; 8482 -0.2; 9330 0.0; 10263 0.0; 11289 -1.7; 12418 -3.0; 13660 -0.1; 15026 -0.0; 16529 -4.2; 18182 -8.3; 20000 -6.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K601 (Dekoni Sheepskin Earpads) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K601 (Dekoni Sheepskin Earpads) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 1.08 | 5.5 dB  |
| Peaking | 186 Hz   | 0.88 | -4.7 dB |
| Peaking | 2441 Hz  | 2.41 | -5.7 dB |
| Peaking | 3505 Hz  | 2.87 | 8.4 dB  |
| Peaking | 18792 Hz | 1.42 | -9.1 dB |
| Peaking | 732 Hz   | 3.09 | 3.2 dB  |
| Peaking | 4279 Hz  | 9.25 | 2.2 dB  |
| Peaking | 5531 Hz  | 5.35 | -2.9 dB |
| Peaking | 12140 Hz | 6.86 | -3.1 dB |
| Peaking | 14756 Hz | 3.73 | 2.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/AKG%20K601%20(Dekoni%20Sheepskin%20Earpads)/AKG%20K601%20(Dekoni%20Sheepskin%20Earpads).png)