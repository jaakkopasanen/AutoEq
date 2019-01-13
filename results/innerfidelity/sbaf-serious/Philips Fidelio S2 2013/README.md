# Philips Fidelio S2 2013
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.1dB
GraphicEQ: 21 -0.7; 23 -1.0; 25 -1.2; 28 -1.4; 31 -1.6; 34 -1.7; 37 -1.8; 41 -2.0; 45 -2.2; 49 -2.3; 54 -2.4; 60 -2.7; 66 -2.8; 72 -3.0; 79 -3.2; 87 -3.5; 96 -3.7; 106 -3.7; 116 -3.6; 128 -3.7; 141 -3.7; 155 -3.6; 170 -3.4; 187 -3.2; 206 -3.0; 227 -2.6; 249 -2.4; 274 -2.0; 302 -1.7; 332 -1.3; 365 -1.0; 402 -0.7; 442 -0.3; 486 -0.2; 535 0.1; 588 0.6; 647 0.7; 712 0.7; 783 0.9; 861 0.6; 947 0.3; 1042 -0.2; 1146 -0.6; 1261 -0.9; 1387 -1.6; 1526 -2.1; 1678 -2.4; 1846 -2.1; 2031 -1.5; 2234 -0.6; 2457 0.7; 2703 1.8; 2973 3.1; 3270 3.9; 3597 3.3; 3957 0.8; 4353 -3.3; 4788 -5.6; 5267 -3.9; 5793 -0.8; 6373 0.7; 7010 1.2; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips Fidelio S2 2013 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-41**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips Fidelio S2 2013 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.6dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 79 Hz   | 0.56 | -2.9 dB  |
| Peaking | 175 Hz  | 1.1  | -2.1 dB  |
| Peaking | 1873 Hz | 1.7  | -4.3 dB  |
| Peaking | 3665 Hz | 0.97 | 6.8 dB   |
| Peaking | 4717 Hz | 2.9  | -11.0 dB |
| Peaking | 720 Hz  | 2.07 | 1.2 dB   |
| Peaking | 1406 Hz | 4.27 | -0.7 dB  |
| Peaking | 5344 Hz | 8.21 | -1.0 dB  |
| Peaking | 6611 Hz | 2.17 | 1.8 dB   |
| Peaking | 7944 Hz | 1.35 | -1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20Fidelio%20S2%202013/Philips%20Fidelio%20S2%202013.png)