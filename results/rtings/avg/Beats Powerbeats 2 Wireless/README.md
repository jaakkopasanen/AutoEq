# Beats Powerbeats 2 Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.9dB
GraphicEQ: 21 -3.8; 23 -4.2; 25 -4.6; 28 -5.1; 31 -5.5; 34 -5.8; 37 -6.1; 41 -6.5; 45 -6.8; 49 -7.1; 54 -7.5; 60 -8.2; 66 -8.9; 72 -9.5; 79 -10.1; 87 -10.8; 96 -11.5; 106 -12.2; 116 -12.9; 128 -13.5; 141 -14.2; 155 -14.8; 170 -15.1; 187 -15.4; 206 -15.5; 227 -15.4; 249 -15.1; 274 -14.6; 302 -14.1; 332 -13.4; 365 -12.6; 402 -11.6; 442 -10.3; 486 -8.8; 535 -6.7; 588 -4.8; 647 -2.8; 712 -1.0; 783 0.3; 861 0.8; 947 0.4; 1042 -0.2; 1146 -0.5; 1261 -0.7; 1387 -0.8; 1526 -0.9; 1678 -1.7; 1846 -3.5; 2031 -5.2; 2234 -5.3; 2457 -4.7; 2703 -2.8; 2973 -0.9; 3270 -0.1; 3597 0.0; 3957 -0.4; 4353 -1.5; 4788 -3.6; 5267 -5.6; 5793 -5.6; 6373 -6.4; 7010 -7.5; 7711 -8.0; 8482 -5.3; 9330 -0.6; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Powerbeats 2 Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-9**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Powerbeats 2 Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 83 Hz    | 0.4  | -8.2 dB |
| Peaking | 200 Hz   | 0.96 | -9.9 dB |
| Peaking | 369 Hz   | 1.77 | -7.0 dB |
| Peaking | 2188 Hz  | 3.73 | -5.7 dB |
| Peaking | 6892 Hz  | 2.02 | -8.2 dB |
| Peaking | 509 Hz   | 3.76 | -1.9 dB |
| Peaking | 826 Hz   | 2.32 | 3.1 dB  |
| Peaking | 3699 Hz  | 2.3  | 4.8 dB  |
| Peaking | 3979 Hz  | 1.17 | -3.3 dB |
| Peaking | 10188 Hz | 3.58 | 2.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Beats%20Powerbeats%202%20Wireless/Beats%20Powerbeats%202%20Wireless.png)