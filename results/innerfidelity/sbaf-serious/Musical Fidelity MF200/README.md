# Musical Fidelity MF200

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.8dB
GraphicEQ: 21 0.0; 23 2.1; 25 1.4; 28 0.6; 31 0.0; 34 -0.5; 37 -1.0; 41 -1.4; 45 -1.8; 49 -2.0; 54 -2.2; 60 -2.3; 66 -2.6; 72 -2.9; 79 -2.9; 87 -3.0; 96 -2.9; 106 -3.2; 116 -3.0; 128 -2.8; 141 -2.4; 155 -2.4; 170 -1.9; 187 -1.7; 206 -1.5; 227 -1.0; 249 -0.5; 274 0.1; 302 1.0; 332 1.6; 365 1.9; 402 2.2; 442 2.9; 486 3.4; 535 4.1; 588 4.1; 647 2.5; 712 1.2; 783 0.6; 861 -0.4; 947 -0.5; 1042 -0.1; 1146 -0.4; 1261 0.3; 1387 0.8; 1526 0.8; 1678 0.7; 1846 0.6; 2031 0.3; 2234 -0.1; 2457 -0.1; 2703 0.0; 2973 -0.1; 3270 -0.2; 3597 -0.4; 3957 0.6; 4353 -0.7; 4788 -3.1; 5267 0.2; 5793 3.5; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.4; 9330 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Musical Fidelity MF200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-57**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Musical Fidelity MF200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 1.36 | 3.8 dB  |
| Peaking | 66 Hz   | 0.69 | -2.4 dB |
| Peaking | 130 Hz  | 1.06 | -1.9 dB |
| Peaking | 504 Hz  | 1.81 | 4.3 dB  |
| Peaking | 6312 Hz | 6.66 | 6.4 dB  |
| Peaking | 595 Hz  | 7.71 | 1.2 dB  |
| Peaking | 926 Hz  | 2.11 | -1.2 dB |
| Peaking | 1501 Hz | 3.12 | 1.0 dB  |
| Peaking | 4782 Hz | 8.34 | -3.7 dB |
| Peaking | 5863 Hz | 6.75 | 1.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Musical%20Fidelity%20MF200/Musical%20Fidelity%20MF200.png)