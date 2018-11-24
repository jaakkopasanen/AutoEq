# Sennheiser Amperior

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 21 0.0; 23 3.2; 25 2.7; 28 2.0; 31 1.3; 34 0.8; 37 0.3; 41 -0.2; 45 -0.6; 49 -0.9; 54 -1.4; 60 -1.8; 66 -2.0; 72 -2.1; 79 -2.9; 87 -3.6; 96 -3.9; 106 -4.5; 116 -4.7; 128 -5.1; 141 -5.2; 155 -5.1; 170 -4.6; 187 -4.4; 206 -3.8; 227 -2.8; 249 -1.8; 274 -1.0; 302 -0.2; 332 0.6; 365 1.3; 402 1.8; 442 2.0; 486 1.7; 535 1.4; 588 1.5; 647 1.2; 712 0.9; 783 0.9; 861 0.5; 947 0.1; 1042 -0.2; 1146 -0.4; 1261 -0.9; 1387 -1.5; 1526 -2.2; 1678 -2.9; 1846 -3.3; 2031 -3.3; 2234 -2.4; 2457 -0.5; 2703 0.9; 2973 2.1; 3270 2.3; 3597 2.2; 3957 2.4; 4353 3.0; 4788 3.2; 5267 4.6; 5793 5.3; 6373 5.5; 7010 2.5; 7711 -1.0; 8482 -5.3; 9330 -4.5; 10263 -0.2; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Amperior GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-59**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Amperior ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 21 Hz   | 1.98 | 4.1 dB   |
| Peaking | 129 Hz  | 1.13 | -5.7 dB  |
| Peaking | 1886 Hz | 2.6  | -4.4 dB  |
| Peaking | 6555 Hz | 0.97 | 7.6 dB   |
| Peaking | 8577 Hz | 2.62 | -11.2 dB |
| Peaking | 209 Hz  | 2.52 | -1.8 dB  |
| Peaking | 444 Hz  | 1.05 | 2.4 dB   |
| Peaking | 1391 Hz | 2.71 | -0.8 dB  |
| Peaking | 3040 Hz | 6.04 | 1.3 dB   |
| Peaking | 4686 Hz | 4.6  | -0.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20Amperior/Sennheiser%20Amperior.png)