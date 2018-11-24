# Beats Studio3 Wireless

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.9; 25 2.4; 28 1.6; 31 0.8; 34 0.2; 37 -0.4; 41 -1.0; 45 -1.6; 49 -2.1; 54 -2.8; 60 -3.5; 66 -3.9; 72 -4.0; 79 -3.8; 87 -3.5; 96 -3.0; 106 -2.6; 116 -2.2; 128 -1.9; 141 -2.0; 155 -2.2; 170 -2.5; 187 -2.9; 206 -3.3; 227 -3.6; 249 -4.0; 274 -4.2; 302 -4.3; 332 -4.6; 365 -4.6; 402 -3.7; 442 -2.4; 486 -0.7; 535 0.9; 588 2.1; 647 2.5; 712 1.7; 783 1.1; 861 0.4; 947 -0.2; 1042 0.3; 1146 0.9; 1261 0.9; 1387 0.8; 1526 0.8; 1678 1.0; 1846 1.5; 2031 2.2; 2234 3.1; 2457 3.9; 2703 3.4; 2973 1.1; 3270 0.3; 3597 1.1; 3957 3.0; 4353 4.9; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -0.2; 10263 -0.7; 11289 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Studio3 Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Studio3 Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.64 | 4.6 dB  |
| Peaking | 67 Hz   | 0.77 | -4.3 dB |
| Peaking | 295 Hz  | 1.73 | -4.7 dB |
| Peaking | 2343 Hz | 2.69 | 3.4 dB  |
| Peaking | 5312 Hz | 2.22 | 6.8 dB  |
| Peaking | 400 Hz  | 4.28 | -2.1 dB |
| Peaking | 619 Hz  | 2.79 | 3.3 dB  |
| Peaking | 3286 Hz | 5.68 | -2.2 dB |
| Peaking | 5987 Hz | 0.6  | 0.9 dB  |
| Peaking | 8986 Hz | 1.64 | -1.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Beats%20Studio3%20Wireless/Beats%20Studio3%20Wireless.png)