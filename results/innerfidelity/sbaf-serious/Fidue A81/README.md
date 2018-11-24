# Fidue A81

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.3dB
GraphicEQ: 21 -2.1; 23 -2.5; 25 -2.8; 28 -3.2; 31 -3.5; 34 -3.8; 37 -4.0; 41 -4.4; 45 -4.6; 49 -4.8; 54 -5.1; 60 -5.4; 66 -5.7; 72 -6.0; 79 -6.3; 87 -6.6; 96 -7.0; 106 -7.1; 116 -7.1; 128 -7.2; 141 -7.3; 155 -7.2; 170 -7.0; 187 -6.8; 206 -6.5; 227 -6.1; 249 -5.7; 274 -5.3; 302 -4.8; 332 -4.2; 365 -3.6; 402 -3.1; 442 -2.4; 486 -1.9; 535 -1.4; 588 -0.6; 647 -0.3; 712 -0.1; 783 0.5; 861 0.4; 947 0.2; 1042 -0.0; 1146 -0.4; 1261 -0.9; 1387 -1.7; 1526 -2.7; 1678 -3.4; 1846 -4.0; 2031 -4.6; 2234 -5.5; 2457 -6.0; 2703 -5.9; 2973 -3.5; 3270 -1.0; 3597 -0.1; 3957 -1.7; 4353 -6.4; 4788 -11.5; 5267 -8.5; 5793 -2.1; 6373 0.8; 7010 1.0; 7711 -1.8; 8482 -6.9; 9330 -8.1; 10263 -5.3; 11289 -3.2; 12418 -0.2; 13660 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fidue A81 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-12**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fidue A81 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 78 Hz    | 0.42 | -5.5 dB  |
| Peaking | 201 Hz   | 0.84 | -3.8 dB  |
| Peaking | 2299 Hz  | 2.1  | -6.0 dB  |
| Peaking | 4891 Hz  | 5.37 | -12.2 dB |
| Peaking | 22064 Hz | 1.67 | -6.4 dB  |
| Peaking | 830 Hz   | 2.17 | 1.4 dB   |
| Peaking | 1608 Hz  | 4.17 | -1.4 dB  |
| Peaking | 6998 Hz  | 3.49 | 5.1 dB   |
| Peaking | 9070 Hz  | 2.12 | -10.2 dB |
| Peaking | 10454 Hz | 0.33 | 1.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fidue%20A81/Fidue%20A81.png)