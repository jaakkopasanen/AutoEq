# Focal Elegia (preliminary)

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 5.4; 72 4.6; 79 3.9; 87 3.4; 96 2.9; 106 2.7; 116 2.6; 128 2.7; 141 2.7; 155 2.8; 170 2.8; 187 2.4; 206 1.9; 227 1.3; 249 1.0; 274 0.8; 302 0.6; 332 0.7; 365 0.8; 402 0.9; 442 1.0; 486 0.9; 535 0.7; 588 0.5; 647 0.6; 712 0.7; 783 0.7; 861 0.5; 947 0.1; 1042 -0.0; 1146 0.1; 1261 0.7; 1387 0.7; 1526 0.3; 1678 0.0; 1846 0.7; 2031 3.8; 2234 5.8; 2457 5.3; 2703 4.8; 2973 4.9; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 4.4; 5267 1.5; 5793 0.4; 6373 4.9; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -1.5; 20000 -13.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Elegia (preliminary) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Elegia (preliminary) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 30 Hz    | 0.11 | 1.9 dB   |
| Peaking | 34 Hz    | 0.5  | 4.5 dB   |
| Peaking | 2298 Hz  | 4.42 | 4.3 dB   |
| Peaking | 3783 Hz  | 1.53 | 6.3 dB   |
| Peaking | 24000 Hz | 2.29 | 1.6 dB   |
| Peaking | 1730 Hz  | 7.3  | -1.6 dB  |
| Peaking | 5649 Hz  | 7.36 | -5.0 dB  |
| Peaking | 6461 Hz  | 3.4  | 5.1 dB   |
| Peaking | 7583 Hz  | 2.86 | -2.2 dB  |
| Peaking | 19801 Hz | 3.41 | -13.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Focal%20Elegia%20(preliminary)/Focal%20Elegia%20(preliminary).png)