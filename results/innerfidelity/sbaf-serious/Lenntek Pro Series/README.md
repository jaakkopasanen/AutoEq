# Lenntek Pro Series

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 5.8; 49 5.7; 54 5.5; 60 5.1; 66 4.8; 72 4.5; 79 4.1; 87 3.6; 96 3.1; 106 2.8; 116 2.6; 128 2.2; 141 1.9; 155 1.7; 170 1.5; 187 1.4; 206 1.3; 227 1.2; 249 1.1; 274 1.2; 302 1.1; 332 1.2; 365 1.3; 402 1.4; 442 1.5; 486 1.4; 535 1.4; 588 1.8; 647 1.8; 712 1.5; 783 1.5; 861 1.0; 947 0.4; 1042 -0.4; 1146 -1.1; 1261 -1.9; 1387 -3.1; 1526 -4.4; 1678 -5.6; 1846 -6.6; 2031 -6.8; 2234 -5.4; 2457 -2.0; 2703 1.3; 2973 4.1; 3270 4.8; 3597 4.1; 3957 1.1; 4353 -3.7; 4788 -0.0; 5267 5.8; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Lenntek Pro Series GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Lenntek Pro Series ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 32 Hz   |  0.38 | 6.3 dB   |
| Peaking | 1060 Hz |  0.55 | 7.6 dB   |
| Peaking | 1976 Hz |  0.59 | -14.0 dB |
| Peaking | 3077 Hz |  2.29 | 12.8 dB  |
| Peaking | 5924 Hz |  3.01 | 9.2 dB   |
| Peaking | 2039 Hz |  8.29 | -0.8 dB  |
| Peaking | 3800 Hz |  6.61 | 3.5 dB   |
| Peaking | 4417 Hz |  4.57 | -5.2 dB  |
| Peaking | 5195 Hz | 10.01 | 3.8 dB   |
| Peaking | 8161 Hz |  0.19 | 0.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Lenntek%20Pro%20Series/Lenntek%20Pro%20Series.png)