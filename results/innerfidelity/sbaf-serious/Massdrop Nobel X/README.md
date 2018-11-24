# Massdrop Nobel X

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -0.8; 23 -0.9; 25 -1.0; 28 -1.1; 31 -1.2; 34 -1.3; 37 -1.5; 41 -1.6; 45 -1.8; 49 -1.9; 54 -2.2; 60 -2.5; 66 -2.8; 72 -3.1; 79 -3.5; 87 -3.8; 96 -4.3; 106 -4.6; 116 -4.7; 128 -5.0; 141 -5.1; 155 -5.3; 170 -5.4; 187 -5.3; 206 -5.3; 227 -5.1; 249 -5.0; 274 -4.7; 302 -4.4; 332 -4.0; 365 -3.6; 402 -3.2; 442 -2.6; 486 -2.3; 535 -1.9; 588 -1.1; 647 -0.7; 712 -0.4; 783 0.1; 861 0.2; 947 0.1; 1042 -0.0; 1146 -0.1; 1261 -0.3; 1387 -0.7; 1526 -1.1; 1678 -1.3; 1846 -1.1; 2031 -0.8; 2234 -0.5; 2457 0.6; 2703 1.6; 2973 3.4; 3270 5.3; 3597 6.0; 3957 5.1; 4353 2.1; 4788 0.4; 5267 2.0; 5793 3.8; 6373 4.3; 7010 2.5; 7711 -0.8; 8482 -4.4; 9330 -4.4; 10263 -1.5; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop Nobel X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop Nobel X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 128 Hz   | 0.53 | -4.3 dB |
| Peaking | 275 Hz   | 0.95 | -2.5 dB |
| Peaking | 3535 Hz  | 3.56 | 6.6 dB  |
| Peaking | 6383 Hz  | 3.59 | 5.2 dB  |
| Peaking | 8796 Hz  | 3.68 | -6.0 dB |
| Peaking | 863 Hz   | 2.27 | 1.0 dB  |
| Peaking | 1935 Hz  | 1.46 | -2.4 dB |
| Peaking | 2593 Hz  | 1.02 | 1.4 dB  |
| Peaking | 4718 Hz  | 9.57 | -1.8 dB |
| Peaking | 11027 Hz | 8.55 | 0.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Massdrop%20Nobel%20X/Massdrop%20Nobel%20X.png)