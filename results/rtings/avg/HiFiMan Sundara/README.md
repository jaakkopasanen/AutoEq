# HiFiMan Sundara

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.9dB
GraphicEQ: 21 0.0; 23 4.9; 25 4.4; 28 3.8; 31 3.3; 34 2.9; 37 2.7; 41 2.3; 45 2.0; 49 1.8; 54 1.6; 60 1.3; 66 1.1; 72 0.9; 79 0.6; 87 0.3; 96 0.0; 106 -0.3; 116 -0.5; 128 -0.8; 141 -1.0; 155 -1.2; 170 -1.3; 187 -1.5; 206 -1.5; 227 -1.6; 249 -1.6; 274 -1.7; 302 -1.8; 332 -2.1; 365 -2.2; 402 -2.2; 442 -1.6; 486 -1.2; 535 -1.7; 588 -1.9; 647 -1.9; 712 -1.8; 783 -1.7; 861 -1.6; 947 -0.5; 1042 0.1; 1146 0.1; 1261 0.2; 1387 0.3; 1526 0.7; 1678 0.7; 1846 1.1; 2031 1.2; 2234 2.7; 2457 1.4; 2703 0.7; 2973 -2.0; 3270 -3.0; 3597 -3.7; 3957 -4.0; 4353 -3.4; 4788 -5.6; 5267 -3.2; 5793 2.2; 6373 -2.3; 7010 -4.5; 7711 -3.6; 8482 -3.5; 9330 -2.0; 10263 0.0; 11289 0.0; 12418 -2.9; 13660 -5.1; 15026 -5.0; 16529 -4.4; 18182 -4.7; 20000 -7.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMan Sundara GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-58**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMan Sundara ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 13 Hz    | 0.44 | 6.5 dB  |
| Peaking | 311 Hz   | 0.59 | -2.1 dB |
| Peaking | 4396 Hz  | 2.2  | -4.6 dB |
| Peaking | 14614 Hz | 1.54 | -4.0 dB |
| Peaking | 20312 Hz | 0.86 | -6.6 dB |
| Peaking | 2475 Hz  | 1.52 | 3.5 dB  |
| Peaking | 3122 Hz  | 3.64 | -3.3 dB |
| Peaking | 5851 Hz  | 7.64 | 7.2 dB  |
| Peaking | 7112 Hz  | 1.45 | -4.1 dB |
| Peaking | 10695 Hz | 3.36 | 3.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/HiFiMan%20Sundara/HiFiMan%20Sundara.png)