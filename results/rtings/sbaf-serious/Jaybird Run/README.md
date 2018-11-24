# Jaybird Run

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.0dB
GraphicEQ: 21 -0.8; 23 -0.9; 25 -1.0; 28 -1.2; 31 -1.3; 34 -1.3; 37 -1.4; 41 -1.5; 45 -1.6; 49 -1.7; 54 -1.8; 60 -2.0; 66 -2.2; 72 -2.3; 79 -2.4; 87 -2.6; 96 -2.9; 106 -3.2; 116 -3.5; 128 -3.9; 141 -4.2; 155 -4.7; 170 -4.9; 187 -5.0; 206 -4.8; 227 -4.5; 249 -4.0; 274 -3.4; 302 -2.7; 332 -2.1; 365 -1.6; 402 -1.0; 442 -0.4; 486 0.4; 535 0.9; 588 1.5; 647 2.0; 712 2.3; 783 2.1; 861 1.4; 947 0.5; 1042 -0.4; 1146 -1.0; 1261 -1.6; 1387 -2.1; 1526 -2.8; 1678 -3.3; 1846 -3.6; 2031 -4.0; 2234 -4.2; 2457 -4.1; 2703 -2.9; 2973 -0.8; 3270 1.6; 3597 3.3; 3957 3.1; 4353 2.4; 4788 2.9; 5267 3.9; 5793 3.1; 6373 -1.8; 7010 -6.4; 7711 -3.2; 8482 -1.3; 9330 -4.0; 10263 -3.4; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jaybird Run GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-39**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jaybird Run ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.2dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 160 Hz  | 0.85 | -5.1 dB  |
| Peaking | 2208 Hz | 1.68 | -5.1 dB  |
| Peaking | 3622 Hz | 3.39 | 3.8 dB   |
| Peaking | 5864 Hz | 1.85 | 13.8 dB  |
| Peaking | 6697 Hz | 1.91 | -15.1 dB |
| Peaking | 37 Hz   | 0.86 | -1.1 dB  |
| Peaking | 708 Hz  | 1.98 | 3.2 dB   |
| Peaking | 1396 Hz | 2.33 | -1.3 dB  |
| Peaking | 9712 Hz | 5.55 | -6.9 dB  |
| Peaking | 9786 Hz | 2.02 | 3.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Jaybird%20Run/Jaybird%20Run.png)