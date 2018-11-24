# Focal Sphear

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.6dB
GraphicEQ: 21 0.0; 23 -0.3; 25 -0.7; 28 -1.3; 31 -1.7; 34 -2.1; 37 -2.5; 41 -2.8; 45 -3.2; 49 -3.5; 54 -3.8; 60 -4.2; 66 -4.5; 72 -4.9; 79 -5.2; 87 -5.7; 96 -6.0; 106 -6.2; 116 -6.2; 128 -6.4; 141 -6.4; 155 -6.4; 170 -6.3; 187 -6.0; 206 -5.9; 227 -5.5; 249 -5.1; 274 -4.7; 302 -4.2; 332 -3.7; 365 -3.2; 402 -2.7; 442 -2.0; 486 -1.7; 535 -1.2; 588 -0.4; 647 -0.1; 712 0.2; 783 0.6; 861 0.4; 947 0.2; 1042 -0.1; 1146 -0.5; 1261 -0.9; 1387 -1.6; 1526 -2.3; 1678 -2.8; 1846 -2.9; 2031 -2.8; 2234 -2.9; 2457 -2.1; 2703 -1.1; 2973 1.0; 3270 2.9; 3597 3.4; 3957 2.0; 4353 -1.3; 4788 -4.2; 5267 -5.7; 5793 -3.3; 6373 -0.3; 7010 1.4; 7711 0.3; 8482 -1.4; 9330 -3.2; 10263 -0.7; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Sphear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-36**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Sphear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 101 Hz  | 0.57 | -5.5 dB |
| Peaking | 229 Hz  | 1.08 | -3.0 dB |
| Peaking | 2041 Hz | 1.79 | -3.5 dB |
| Peaking | 3519 Hz | 3.23 | 5.1 dB  |
| Peaking | 5126 Hz | 4.11 | -6.5 dB |
| Peaking | 15 Hz   | 2.01 | 1.3 dB  |
| Peaking | 787 Hz  | 0.71 | -1.9 dB |
| Peaking | 789 Hz  | 1.26 | 3.3 dB  |
| Peaking | 7045 Hz | 5.91 | 2.4 dB  |
| Peaking | 9250 Hz | 6.11 | -3.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Focal%20Sphear/Focal%20Sphear.png)