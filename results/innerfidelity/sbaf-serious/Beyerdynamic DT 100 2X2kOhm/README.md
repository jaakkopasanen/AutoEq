# Beyerdynamic DT 100 2X2kOhm

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.2dB
GraphicEQ: 21 0.0; 23 3.3; 25 2.7; 28 1.9; 31 1.3; 34 0.8; 37 0.3; 41 -0.2; 45 -0.5; 49 -0.8; 54 -1.2; 60 -1.3; 66 -1.5; 72 -1.6; 79 -1.2; 87 -2.4; 96 -1.9; 106 -0.8; 116 -4.3; 128 -7.9; 141 -8.8; 155 -8.2; 170 -7.6; 187 -9.5; 206 -9.2; 227 -8.9; 249 -8.7; 274 -8.3; 302 -7.8; 332 -7.3; 365 -6.6; 402 -6.0; 442 -5.0; 486 -4.5; 535 -3.7; 588 -2.6; 647 -1.9; 712 -1.6; 783 -1.0; 861 -0.6; 947 -0.3; 1042 0.6; 1146 0.3; 1261 0.3; 1387 -0.5; 1526 -2.3; 1678 -3.6; 1846 -4.3; 2031 -3.4; 2234 -2.0; 2457 -0.4; 2703 2.2; 2973 3.8; 3270 4.1; 3597 3.2; 3957 2.8; 4353 3.1; 4788 4.8; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 -0.6; 8482 -4.5; 9330 -5.7; 10263 -0.4; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 100 2X2kOhm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 100 2X2kOhm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 1.64 | 4.1 dB  |
| Peaking | 139 Hz  | 4.45 | -4.5 dB |
| Peaking | 246 Hz  | 0.79 | -9.1 dB |
| Peaking | 5646 Hz | 1.38 | 6.8 dB  |
| Peaking | 8852 Hz | 3.63 | -8.4 dB |
| Peaking | 107 Hz  | 6.48 | 4.5 dB  |
| Peaking | 113 Hz  | 2.79 | -1.7 dB |
| Peaking | 1264 Hz | 1.44 | 4.7 dB  |
| Peaking | 1768 Hz | 1.2  | -6.8 dB |
| Peaking | 2976 Hz | 2.94 | 4.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%20100%202X2kOhm/Beyerdynamic%20DT%20100%202X2kOhm.png)