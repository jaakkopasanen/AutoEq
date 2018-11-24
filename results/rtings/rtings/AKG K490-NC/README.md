# AKG K490-NC

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 5.8; 31 5.4; 34 5.0; 37 4.6; 41 4.1; 45 3.8; 49 3.4; 54 2.9; 60 2.2; 66 1.5; 72 0.8; 79 0.2; 87 -0.6; 96 -1.3; 106 -2.1; 116 -2.9; 128 -3.5; 141 -3.9; 155 -4.2; 170 -4.4; 187 -4.3; 206 -4.1; 227 -4.2; 249 -4.4; 274 -4.7; 302 -4.8; 332 -5.0; 365 -5.7; 402 -6.0; 442 -6.1; 486 -6.3; 535 -6.4; 588 -6.4; 647 -6.1; 712 -5.4; 783 -4.3; 861 -2.6; 947 -0.7; 1042 -0.0; 1146 -1.2; 1261 -2.7; 1387 -4.1; 1526 -4.5; 1678 -4.0; 1846 -2.5; 2031 -1.0; 2234 -0.6; 2457 -0.1; 2703 0.1; 2973 -1.3; 3270 -2.7; 3597 -4.0; 3957 -2.4; 4353 1.6; 4788 4.8; 5267 1.7; 5793 1.0; 6373 3.8; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 -0.3; 11289 -4.4; 12418 -7.8; 13660 -7.5; 15026 -4.9; 16529 -6.3; 18182 -6.7; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K490-NC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K490-NC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 0.59 | 6.3 dB  |
| Peaking | 325 Hz   | 0.38 | -5.9 dB |
| Peaking | 1566 Hz  | 4.98 | -3.5 dB |
| Peaking | 12985 Hz | 3.33 | -8.2 dB |
| Peaking | 17298 Hz | 2.07 | -7.7 dB |
| Peaking | 629 Hz   | 2.58 | -2.0 dB |
| Peaking | 1005 Hz  | 4.79 | 3.5 dB  |
| Peaking | 3639 Hz  | 4.8  | -4.4 dB |
| Peaking | 4723 Hz  | 6.13 | 5.7 dB  |
| Peaking | 6608 Hz  | 5.71 | 4.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/AKG%20K490-NC/AKG%20K490-NC.png)