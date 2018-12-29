# Skullcandy Holua
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.0dB
GraphicEQ: 21 -9.9; 23 -9.9; 25 -9.8; 28 -9.6; 31 -9.5; 34 -9.4; 37 -9.2; 41 -9.1; 45 -9.0; 49 -8.8; 54 -8.7; 60 -8.6; 66 -8.5; 72 -8.4; 79 -8.3; 87 -8.2; 96 -8.1; 106 -7.9; 116 -7.6; 128 -7.4; 141 -7.1; 155 -6.8; 170 -6.3; 187 -5.9; 206 -5.4; 227 -4.9; 249 -4.4; 274 -3.8; 302 -3.3; 332 -2.7; 365 -2.2; 402 -1.7; 442 -1.0; 486 -0.7; 535 -0.3; 588 0.4; 647 0.7; 712 0.7; 783 1.0; 861 0.8; 947 0.4; 1042 -0.3; 1146 -0.7; 1261 -1.3; 1387 -2.3; 1526 -3.5; 1678 -4.5; 1846 -5.5; 2031 -6.6; 2234 -8.4; 2457 -8.4; 2703 -4.9; 2973 -1.1; 3270 2.2; 3597 3.4; 3957 1.1; 4353 -3.3; 4788 -10.1; 5267 -5.4; 5793 1.0; 6373 4.8; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Holua GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-50**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Holua ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.5dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 23 Hz   |  0.21 | -9.6 dB  |
| Peaking | 154 Hz  |  0.82 | -3.5 dB  |
| Peaking | 2348 Hz |  1.69 | -14.7 dB |
| Peaking | 3630 Hz |  0.83 | 9.8 dB   |
| Peaking | 4768 Hz |  4.89 | -16.6 dB |
| Peaking | 757 Hz  |  1.88 | 1.8 dB   |
| Peaking | 1583 Hz |  4.28 | -1.5 dB  |
| Peaking | 5242 Hz | 10.16 | -2.8 dB  |
| Peaking | 6427 Hz |  4.84 | 4.8 dB   |
| Peaking | 8165 Hz |  1.69 | -2.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Skullcandy%20Holua/Skullcandy%20Holua.png)