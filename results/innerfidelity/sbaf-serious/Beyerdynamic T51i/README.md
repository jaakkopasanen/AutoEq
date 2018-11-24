# Beyerdynamic T51i

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 21 0.0; 23 -0.4; 25 -0.9; 28 -1.6; 31 -2.2; 34 -2.7; 37 -3.1; 41 -3.6; 45 -3.9; 49 -4.3; 54 -4.9; 60 -5.5; 66 -5.8; 72 -6.1; 79 -6.5; 87 -6.7; 96 -6.9; 106 -7.4; 116 -7.7; 128 -7.4; 141 -7.8; 155 -7.6; 170 -6.9; 187 -6.6; 206 -5.7; 227 -4.7; 249 -3.9; 274 -3.0; 302 -2.5; 332 -2.7; 365 -3.1; 402 -3.4; 442 -3.2; 486 -3.0; 535 -2.8; 588 -2.1; 647 -1.9; 712 -1.7; 783 -0.6; 861 -0.1; 947 -0.1; 1042 0.1; 1146 0.5; 1261 0.9; 1387 1.1; 1526 1.5; 1678 2.3; 1846 3.7; 2031 4.9; 2234 3.6; 2457 1.8; 2703 1.7; 2973 3.2; 3270 4.7; 3597 5.5; 3957 5.5; 4353 3.5; 4788 1.7; 5267 3.9; 5793 5.8; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -2.2; 9330 -4.6; 10263 -1.3; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T51i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T51i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 52 Hz   | 1.59 | -0.7 dB |
| Peaking | 122 Hz  | 0.47 | -7.4 dB |
| Peaking | 1972 Hz | 2.94 | 4.5 dB  |
| Peaking | 3662 Hz | 3.04 | 5.7 dB  |
| Peaking | 5997 Hz | 4.77 | 6.1 dB  |
| Peaking | 288 Hz  | 2.16 | 2.7 dB  |
| Peaking | 660 Hz  | 0.48 | -2.8 dB |
| Peaking | 968 Hz  | 0.89 | 2.8 dB  |
| Peaking | 8560 Hz | 1.13 | 1.5 dB  |
| Peaking | 9208 Hz | 3.86 | -6.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T51i/Beyerdynamic%20T51i.png)