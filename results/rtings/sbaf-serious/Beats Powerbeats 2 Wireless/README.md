# Beats Powerbeats 2 Wireless

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.3dB
GraphicEQ: 21 -3.4; 23 -3.9; 25 -4.3; 28 -4.9; 31 -5.4; 34 -5.8; 37 -6.2; 41 -6.7; 45 -7.1; 49 -7.4; 54 -7.8; 60 -8.5; 66 -9.1; 72 -9.5; 79 -9.9; 87 -10.5; 96 -11.1; 106 -11.8; 116 -12.4; 128 -13.0; 141 -13.7; 155 -14.2; 170 -14.5; 187 -14.8; 206 -15.0; 227 -14.9; 249 -14.5; 274 -14.0; 302 -13.3; 332 -12.5; 365 -11.6; 402 -10.5; 442 -9.2; 486 -7.6; 535 -5.5; 588 -3.7; 647 -1.8; 712 -0.2; 783 0.8; 861 1.0; 947 0.4; 1042 -0.2; 1146 -0.3; 1261 -0.5; 1387 -0.8; 1526 -1.3; 1678 -2.0; 1846 -3.4; 2031 -4.8; 2234 -4.9; 2457 -4.2; 2703 -2.0; 2973 0.7; 3270 2.5; 3597 3.2; 3957 2.0; 4353 -0.2; 4788 -2.0; 5267 -2.7; 5793 -1.7; 6373 -2.6; 7010 -4.1; 7711 -5.5; 8482 -4.2; 9330 -0.6; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Powerbeats 2 Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-33**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Powerbeats 2 Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 81 Hz   | 0.41 | -8.3 dB |
| Peaking | 202 Hz  | 1.02 | -9.7 dB |
| Peaking | 360 Hz  | 1.86 | -6.4 dB |
| Peaking | 2146 Hz | 4.11 | -5.5 dB |
| Peaking | 7596 Hz | 3.21 | -5.7 dB |
| Peaking | 494 Hz  | 3.89 | -1.9 dB |
| Peaking | 803 Hz  | 2.04 | 3.2 dB  |
| Peaking | 3596 Hz | 2.48 | 8.1 dB  |
| Peaking | 4143 Hz | 0.85 | -5.0 dB |
| Peaking | 7173 Hz | 0.69 | 1.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Beats%20Powerbeats%202%20Wireless/Beats%20Powerbeats%202%20Wireless.png)