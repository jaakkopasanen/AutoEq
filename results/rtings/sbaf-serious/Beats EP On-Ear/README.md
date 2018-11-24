# Beats EP On-Ear

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -0.8; 23 -1.0; 25 -1.1; 28 -1.4; 31 -1.6; 34 -1.8; 37 -1.9; 41 -2.0; 45 -2.1; 49 -2.2; 54 -2.4; 60 -2.7; 66 -3.0; 72 -3.1; 79 -3.2; 87 -3.3; 96 -3.5; 106 -3.8; 116 -4.0; 128 -4.3; 141 -4.5; 155 -4.5; 170 -4.5; 187 -4.5; 206 -4.4; 227 -4.2; 249 -3.6; 274 -2.9; 302 -2.1; 332 -1.7; 365 -1.2; 402 -1.2; 442 -0.9; 486 -0.5; 535 -0.1; 588 0.3; 647 0.6; 712 0.8; 783 0.6; 861 0.4; 947 0.1; 1042 0.0; 1146 -0.0; 1261 -0.2; 1387 -0.8; 1526 -1.6; 1678 -1.9; 1846 -1.8; 2031 -1.7; 2234 -0.8; 2457 0.4; 2703 1.5; 2973 1.8; 3270 2.5; 3597 3.4; 3957 3.0; 4353 0.8; 4788 -1.2; 5267 2.8; 5793 5.9; 6373 5.2; 7010 2.3; 7711 0.1; 8482 -2.4; 9330 -3.4; 10263 -0.3; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats EP On-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats EP On-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 79 Hz   | 0.51 | -2.8 dB |
| Peaking | 189 Hz  | 1.17 | -3.4 dB |
| Peaking | 3581 Hz | 4.61 | 3.7 dB  |
| Peaking | 6068 Hz | 4.55 | 6.7 dB  |
| Peaking | 8999 Hz | 4.8  | -4.2 dB |
| Peaking | 715 Hz  | 2    | 1.2 dB  |
| Peaking | 1828 Hz | 2.13 | -2.3 dB |
| Peaking | 2752 Hz | 4.9  | 1.6 dB  |
| Peaking | 4801 Hz | 7.15 | -4.9 dB |
| Peaking | 4938 Hz | 2.84 | 2.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Beats%20EP%20On-Ear/Beats%20EP%20On-Ear.png)