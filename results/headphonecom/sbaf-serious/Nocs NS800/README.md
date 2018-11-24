# Nocs NS800

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -0.3; 23 -0.3; 25 -0.3; 28 -0.3; 31 -0.4; 34 -0.4; 37 -0.5; 41 -0.6; 45 -0.7; 49 -0.9; 54 -1.1; 60 -1.4; 66 -1.5; 72 -1.7; 79 -2.0; 87 -2.3; 96 -2.4; 106 -2.7; 116 -2.7; 128 -3.0; 141 -3.0; 155 -3.3; 170 -3.2; 187 -3.3; 206 -3.2; 227 -3.1; 249 -3.1; 274 -2.8; 302 -2.6; 332 -2.3; 365 -2.0; 402 -1.7; 442 -1.4; 486 -1.2; 535 -0.8; 588 -0.5; 647 -0.2; 712 0.3; 783 0.4; 861 0.3; 947 0.2; 1042 -0.1; 1146 -0.4; 1261 -0.7; 1387 -1.1; 1526 -1.6; 1678 -1.7; 1846 -1.5; 2031 -1.2; 2234 -1.0; 2457 -0.8; 2703 -1.0; 2973 -0.5; 3270 2.7; 3597 5.9; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Nocs NS800 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Nocs NS800 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 131 Hz  | 0.66 | -2.7 dB |
| Peaking | 266 Hz  | 1.2  | -1.7 dB |
| Peaking | 1831 Hz | 1.87 | -2.6 dB |
| Peaking | 2822 Hz | 4.18 | -3.6 dB |
| Peaking | 4416 Hz | 1.23 | 7.3 dB  |
| Peaking | 798 Hz  | 3.29 | 0.9 dB  |
| Peaking | 3567 Hz | 7.92 | 2.2 dB  |
| Peaking | 6258 Hz | 0.94 | -2.6 dB |
| Peaking | 6283 Hz | 2.65 | 5.2 dB  |
| Peaking | 7518 Hz | 3.31 | -1.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Nocs%20NS800/Nocs%20NS800.png)