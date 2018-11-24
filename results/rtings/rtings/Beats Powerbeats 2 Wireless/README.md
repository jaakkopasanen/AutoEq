# Beats Powerbeats 2 Wireless

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.3dB
GraphicEQ: 21 -3.8; 23 -4.2; 25 -4.6; 28 -5.1; 31 -5.5; 34 -5.8; 37 -6.1; 41 -6.5; 45 -6.8; 49 -7.1; 54 -7.5; 60 -8.2; 66 -8.9; 72 -9.5; 79 -10.1; 87 -10.8; 96 -11.5; 106 -12.2; 116 -12.9; 128 -13.5; 141 -14.2; 155 -14.8; 170 -15.1; 187 -15.4; 206 -15.5; 227 -15.4; 249 -15.1; 274 -14.6; 302 -14.1; 332 -13.4; 365 -12.6; 402 -11.6; 442 -10.3; 486 -8.8; 535 -6.7; 588 -4.8; 647 -2.8; 712 -1.0; 783 0.3; 861 0.8; 947 0.4; 1042 -0.2; 1146 -0.5; 1261 -0.7; 1387 -0.8; 1526 -0.9; 1678 -1.7; 1846 -3.5; 2031 -5.2; 2234 -5.4; 2457 -4.7; 2703 -2.6; 2973 -0.4; 3270 0.6; 3597 1.0; 3957 0.8; 4353 -0.2; 4788 -1.8; 5267 -3.1; 5793 -3.1; 6373 -5.2; 7010 -6.6; 7711 -6.6; 8482 -4.6; 9330 -1.8; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Powerbeats 2 Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-12**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Powerbeats 2 Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 84 Hz    | 0.39 | -8.2 dB |
| Peaking | 201 Hz   | 0.95 | -9.9 dB |
| Peaking | 369 Hz   | 1.77 | -7.0 dB |
| Peaking | 2183 Hz  | 3.88 | -5.9 dB |
| Peaking | 7229 Hz  | 2.63 | -7.4 dB |
| Peaking | 24 Hz    | 2.14 | -1.1 dB |
| Peaking | 505 Hz   | 4.24 | -1.8 dB |
| Peaking | 824 Hz   | 2.73 | 3.1 dB  |
| Peaking | 3647 Hz  | 5.04 | 2.2 dB  |
| Peaking | 21018 Hz | 2.59 | 0.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Beats%20Powerbeats%202%20Wireless/Beats%20Powerbeats%202%20Wireless.png)