# HiFiMan Sundara

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.4dB
GraphicEQ: 21 0.0; 23 5.3; 25 4.7; 28 3.9; 31 3.3; 34 2.9; 37 2.5; 41 2.1; 45 1.8; 49 1.5; 54 1.3; 60 1.0; 66 0.9; 72 0.9; 79 0.8; 87 0.7; 96 0.5; 106 0.2; 116 -0.0; 128 -0.3; 141 -0.4; 155 -0.6; 170 -0.7; 187 -0.9; 206 -1.0; 227 -1.1; 249 -1.0; 274 -1.0; 302 -1.0; 332 -1.1; 365 -1.2; 402 -1.2; 442 -0.5; 486 0.0; 535 -0.5; 588 -0.8; 647 -0.9; 712 -1.0; 783 -1.2; 861 -1.5; 947 -0.5; 1042 0.1; 1146 0.3; 1261 0.5; 1387 0.3; 1526 0.4; 1678 0.3; 1846 1.1; 2031 1.6; 2234 3.2; 2457 1.8; 2703 1.5; 2973 -0.5; 3270 -0.4; 3597 -0.5; 3957 -1.5; 4353 -2.1; 4788 -4.0; 5267 -0.3; 5793 5.9; 6373 1.5; 7010 -1.3; 7711 -2.1; 8482 -4.0; 9330 -3.1; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMan Sundara GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-63**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMan Sundara ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 0.92 | 5.9 dB  |
| Peaking | 2247 Hz  | 3.94 | 3.3 dB  |
| Peaking | 4832 Hz  | 2.98 | -4.8 dB |
| Peaking | 5733 Hz  | 6.4  | 8.8 dB  |
| Peaking | 8544 Hz  | 4.2  | -4.5 dB |
| Peaking | 266 Hz   | 0.98 | -1.2 dB |
| Peaking | 846 Hz   | 2.35 | -2.0 dB |
| Peaking | 1044 Hz  | 2.02 | 1.2 dB  |
| Peaking | 10303 Hz | 7.57 | 1.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/HiFiMan%20Sundara/HiFiMan%20Sundara.png)