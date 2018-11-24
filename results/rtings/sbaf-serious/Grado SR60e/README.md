# Grado SR60e

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.5; 34 4.7; 37 3.9; 41 2.9; 45 2.0; 49 1.3; 54 0.6; 60 -0.0; 66 -0.5; 72 -0.8; 79 -1.0; 87 -1.1; 96 -1.2; 106 -1.4; 116 -1.6; 128 -1.7; 141 -1.6; 155 -1.5; 170 -1.3; 187 -1.2; 206 -1.0; 227 -0.9; 249 -0.8; 274 -0.6; 302 -0.3; 332 -0.2; 365 -0.8; 402 -0.8; 442 -0.6; 486 -0.2; 535 -0.1; 588 0.0; 647 0.2; 712 0.3; 783 0.1; 861 -0.1; 947 -0.0; 1042 0.1; 1146 0.2; 1261 -0.0; 1387 -0.8; 1526 -1.9; 1678 -3.2; 1846 -6.4; 2031 -8.4; 2234 -7.4; 2457 -5.7; 2703 -3.8; 2973 -1.9; 3270 -0.5; 3597 -2.2; 3957 -4.6; 4353 -2.0; 4788 0.8; 5267 -0.1; 5793 0.2; 6373 -1.8; 7010 -4.0; 7711 -6.1; 8482 -9.5; 9330 -10.7; 10263 -6.0; 11289 -0.1; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR60e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR60e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 25 Hz    | 0.85 | 6.8 dB   |
| Peaking | 91 Hz    | 0.55 | -2.2 dB  |
| Peaking | 2100 Hz  | 3    | -8.9 dB  |
| Peaking | 3941 Hz  | 8.1  | -3.9 dB  |
| Peaking | 8939 Hz  | 3.36 | -11.8 dB |
| Peaking | 1289 Hz  | 1.34 | 1.8 dB   |
| Peaking | 1634 Hz  | 1.17 | -1.3 dB  |
| Peaking | 5689 Hz  | 2.36 | 2.8 dB   |
| Peaking | 6852 Hz  | 2.14 | -2.3 dB  |
| Peaking | 11688 Hz | 4.85 | 2.3 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Grado%20SR60e/Grado%20SR60e.png)