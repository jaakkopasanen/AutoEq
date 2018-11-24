# Fidue A83

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.2; 23 -1.5; 25 -1.8; 28 -2.1; 31 -2.4; 34 -2.6; 37 -2.8; 41 -3.0; 45 -3.2; 49 -3.4; 54 -3.6; 60 -4.0; 66 -4.3; 72 -4.5; 79 -4.7; 87 -5.1; 96 -5.4; 106 -5.5; 116 -5.5; 128 -5.6; 141 -5.7; 155 -5.6; 170 -5.5; 187 -5.3; 206 -5.0; 227 -4.6; 249 -4.3; 274 -3.8; 302 -3.4; 332 -2.8; 365 -2.4; 402 -1.9; 442 -1.2; 486 -0.9; 535 0.4; 588 0.8; 647 1.1; 712 1.1; 783 1.4; 861 1.0; 947 0.5; 1042 -0.3; 1146 -1.2; 1261 -2.5; 1387 -4.3; 1526 -6.2; 1678 -7.2; 1846 -6.8; 2031 -5.4; 2234 -4.3; 2457 -3.8; 2703 -4.4; 2973 -2.3; 3270 2.0; 3597 5.9; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 5.9; 6373 3.4; 7010 -2.6; 7711 -8.2; 8482 -10.4; 9330 -8.6; 10263 -3.7; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fidue A83 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fidue A83 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 134 Hz   | 0.37 | -6.0 dB  |
| Peaking | 1693 Hz  | 1.31 | -15.6 dB |
| Peaking | 2762 Hz  | 1.76 | -14.1 dB |
| Peaking | 3292 Hz  | 0.38 | 17.5 dB  |
| Peaking | 8431 Hz  | 1.88 | -19.6 dB |
| Peaking | 626 Hz   | 4.74 | 0.7 dB   |
| Peaking | 4690 Hz  | 4.03 | -1.7 dB  |
| Peaking | 6221 Hz  | 2.27 | 2.8 dB   |
| Peaking | 7293 Hz  | 6.3  | -3.5 dB  |
| Peaking | 16363 Hz | 1.55 | -1.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fidue%20A83/Fidue%20A83.png)