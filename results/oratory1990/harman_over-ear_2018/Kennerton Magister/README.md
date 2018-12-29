# Kennerton Magister

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.1; 25 2.6; 28 2.0; 31 1.6; 34 1.3; 37 1.0; 41 0.6; 45 0.3; 49 -0.0; 54 -0.3; 60 -0.2; 66 0.4; 72 0.8; 79 -0.6; 87 -2.7; 96 -2.7; 106 -4.1; 116 -5.0; 128 -5.5; 141 -5.8; 155 -5.8; 170 -5.5; 187 -5.1; 206 -5.0; 227 -3.8; 249 -1.8; 274 1.0; 302 4.5; 332 6.0; 365 5.9; 402 3.6; 442 1.7; 486 1.1; 535 0.1; 588 -0.5; 647 -0.5; 712 -0.1; 783 0.4; 861 0.4; 947 0.2; 1042 0.2; 1146 0.6; 1261 1.2; 1387 1.9; 1526 2.6; 1678 3.3; 1846 3.6; 2031 4.0; 2234 3.9; 2457 2.7; 2703 1.4; 2973 0.6; 3270 0.3; 3597 4.8; 3957 1.2; 4353 -1.1; 4788 -4.2; 5267 -6.7; 5793 -5.9; 6373 3.9; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 -0.0; 13660 -3.1; 15026 -7.5; 16529 -8.9; 18182 -6.3; 20000 -1.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kennerton Magister GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kennerton Magister ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 168 Hz   | 1    | -6.8 dB  |
| Peaking | 334 Hz   | 2.85 | 8.8 dB   |
| Peaking | 4576 Hz  | 0.34 | 3.7 dB   |
| Peaking | 5166 Hz  | 3.65 | -11.1 dB |
| Peaking | 16485 Hz | 1.33 | -10.3 dB |
| Peaking | 12 Hz    | 1.15 | 1.1 dB   |
| Peaking | 14 Hz    | 0.63 | 4.4 dB   |
| Peaking | 2040 Hz  | 2.92 | 2.3 dB   |
| Peaking | 3195 Hz  | 2.52 | -3.2 dB  |
| Peaking | 3657 Hz  | 9.82 | 5.6 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Kennerton%20Magister/Kennerton%20Magister.png)