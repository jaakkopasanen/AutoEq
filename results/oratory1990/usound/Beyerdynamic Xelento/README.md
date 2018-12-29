# Beyerdynamic Xelento

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.7dB
GraphicEQ: 21 -7.6; 23 -7.5; 25 -7.4; 28 -7.4; 31 -7.3; 34 -7.2; 37 -7.1; 41 -6.9; 45 -6.8; 49 -6.7; 54 -6.5; 60 -6.4; 66 -6.3; 72 -6.2; 79 -6.1; 87 -5.9; 96 -5.9; 106 -5.8; 116 -5.8; 128 -5.6; 141 -5.3; 155 -5.1; 170 -5.6; 187 -5.7; 206 -5.2; 227 -4.6; 249 -4.1; 274 -3.5; 302 -3.0; 332 -2.7; 365 -2.5; 402 -2.2; 442 -1.8; 486 -1.4; 535 -1.0; 588 -0.8; 647 -0.5; 712 -0.2; 783 0.2; 861 0.3; 947 0.1; 1042 -0.0; 1146 -0.4; 1261 -1.0; 1387 -1.2; 1526 -1.0; 1678 -0.6; 1846 0.0; 2031 0.4; 2234 0.7; 2457 0.8; 2703 1.1; 2973 1.5; 3270 1.9; 3597 2.2; 3957 1.8; 4353 0.8; 4788 -1.6; 5267 -3.8; 5793 1.4; 6373 5.5; 7010 2.5; 7711 -1.0; 8482 -3.2; 9330 -3.1; 10263 -1.7; 11289 -1.3; 12418 -0.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic Xelento GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-57**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic Xelento ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 43 Hz   | 0.27 | -6.0 dB |
| Peaking | 202 Hz  | 0.91 | -2.7 dB |
| Peaking | 6463 Hz | 7.05 | 6.9 dB  |
| Peaking | 8924 Hz | 2.81 | -3.8 dB |
| Peaking | 16 Hz   | 0.84 | -2.7 dB |
| Peaking | 855 Hz  | 3.13 | 0.8 dB  |
| Peaking | 1427 Hz | 2.72 | -1.5 dB |
| Peaking | 3848 Hz | 1.08 | 2.4 dB  |
| Peaking | 5141 Hz | 5.7  | -6.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Beyerdynamic%20Xelento/Beyerdynamic%20Xelento.png)