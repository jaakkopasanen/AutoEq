# MEE A161P

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.3; 25 2.2; 28 2.1; 31 2.1; 34 2.0; 37 1.8; 41 1.6; 45 1.5; 49 1.3; 54 1.1; 60 0.8; 66 0.5; 72 0.2; 79 -0.2; 87 -0.6; 96 -1.1; 106 -1.3; 116 -1.6; 128 -1.9; 141 -2.3; 155 -2.5; 170 -2.5; 187 -2.7; 206 -2.7; 227 -2.7; 249 -2.7; 274 -2.6; 302 -2.4; 332 -2.2; 365 -2.0; 402 -1.8; 442 -1.4; 486 -1.2; 535 -0.8; 588 -0.2; 647 0.1; 712 0.2; 783 0.6; 861 0.3; 947 0.1; 1042 -0.1; 1146 -0.3; 1261 -0.6; 1387 -1.0; 1526 -1.6; 1678 -2.0; 1846 -2.2; 2031 -2.5; 2234 -3.2; 2457 -3.4; 2703 -2.0; 2973 2.6; 3270 5.9; 3597 6.0; 3957 6.0; 4353 5.0; 4788 2.0; 5267 -1.2; 5793 -3.9; 6373 1.7; 7010 2.5; 7711 0.3; 8482 -0.2; 9330 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MEE A161P GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MEE A161P ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 25 Hz   | 0.49 | 2.4 dB   |
| Peaking | 195 Hz  | 0.69 | -3.0 dB  |
| Peaking | 2544 Hz | 1.53 | -10.4 dB |
| Peaking | 3344 Hz | 1.31 | 12.0 dB  |
| Peaking | 5577 Hz | 6.89 | -7.3 dB  |
| Peaking | 397 Hz  | 2.06 | -0.6 dB  |
| Peaking | 761 Hz  | 1.89 | 1.0 dB   |
| Peaking | 1583 Hz | 4.35 | -0.9 dB  |
| Peaking | 6744 Hz | 8.76 | 3.5 dB   |
| Peaking | 8104 Hz | 1.58 | -1.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/MEE%20A161P/MEE%20A161P.png)