# Jaybird X3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.7dB
GraphicEQ: 21 -0.7; 23 -0.8; 25 -0.8; 28 -0.9; 31 -1.0; 34 -1.1; 37 -1.1; 41 -1.2; 45 -1.2; 49 -1.3; 54 -1.4; 60 -1.7; 66 -1.9; 72 -1.9; 79 -2.0; 87 -2.2; 96 -2.5; 106 -3.0; 116 -3.4; 128 -3.7; 141 -3.9; 155 -4.0; 170 -3.9; 187 -4.1; 206 -4.4; 227 -4.3; 249 -3.8; 274 -3.0; 302 -2.4; 332 -1.7; 365 -1.1; 402 -0.5; 442 0.2; 486 1.0; 535 1.6; 588 2.1; 647 2.7; 712 2.7; 783 2.2; 861 1.5; 947 0.5; 1042 -0.3; 1146 -0.7; 1261 -1.1; 1387 -1.5; 1526 -2.0; 1678 -2.4; 1846 -2.5; 2031 -2.7; 2234 -2.7; 2457 -2.6; 2703 -2.1; 2973 -0.2; 3270 2.2; 3597 3.9; 3957 3.8; 4353 2.9; 4788 3.8; 5267 5.3; 5793 5.4; 6373 1.8; 7010 -3.6; 7711 -4.0; 8482 -1.1; 9330 -1.4; 10263 -3.5; 11289 -0.4; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jaybird X3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-57**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jaybird X3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 158 Hz   |  0.89 | -4.5 dB |
| Peaking | 2240 Hz  |  1.72 | -3.6 dB |
| Peaking | 3637 Hz  |  3.49 | 4.2 dB  |
| Peaking | 5829 Hz  |  2.2  | 10.1 dB |
| Peaking | 7057 Hz  |  2.02 | -8.6 dB |
| Peaking | 37 Hz    |  0.94 | -0.9 dB |
| Peaking | 257 Hz   |  2.85 | -1.5 dB |
| Peaking | 675 Hz   |  1.55 | 3.5 dB  |
| Peaking | 1303 Hz  |  1.74 | -1.3 dB |
| Peaking | 10343 Hz | 10.53 | -3.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Jaybird%20X3/Jaybird%20X3.png)